#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import io
import threading
import socket
import logging
import utility
from network.message_handler import MessageHandler, MessageError
from network.server.request_handler import RequestHandler, UnknownRequest


PORT = utility.getConfig('port')


class NetConnector:
    running: bool = None
    thread: threading.Thread = None

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.handler = RequestHandler()

    def join(self):
        try:
            self.socket.bind(("", PORT))
        except Exception:
            self.socket.close()
            raise
        else:
            self.thread = threading.Thread(target=self.run, name="filius-server", daemon=False)
            self.thread.start()

    def leave(self):
        self.running = False
        self.thread.join(timeout=10)
        if self.thread.is_alive():
            logging.warning(f"thread failed to stop ({self.thread})")

    def run(self):
        self.running = True
        while self.running:
            try:
                self.iteration()
            except (threading.ThreadError, InterruptedError):
                break
            except Exception as exc:
                logging.error(str(exc), exc_info=exc)

    def iteration(self):
        try:
            message, address = self.receive()
        except MessageError:
            return
        try:
            answer = self.handler.handleRequest(message)
        except UnknownRequest:
            return
        self.send(answer, address=address)

    def receive(self):
        buffer = io.BytesIO()
        _, address = self.socket.recvfrom_into(buffer)
        message = MessageHandler.decryptData(buffer.getvalue())
        return message, address

    def send(self, message, *, address='255.255.255.255'):
        address = (address, PORT)
        data = MessageHandler.encryptMessage(message)
        nbytes = self.socket.sendto(data, address)
        print("Send some bytes", [nbytes, "of", len(data)])

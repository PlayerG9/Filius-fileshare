#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import time
import typing as t
import socket
import threading
import utility
from network.message_handler import MessageHandler

Member = t.Tuple[str, int]

PORT = utility.getConfig('port') + 1


class NetMemberList:
    members: {Member}
    thread: threading.Thread = None

    def __init__(self):
        self.members = set()
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.setblocking(False)

    def __enter__(self):
        try:
            self.socket.bind(("", PORT))
            self.socket.listen()
        except Exception:
            self.socket.close()
            raise
        else:
            self.thread = threading.Thread(target=self.run)
            self.thread.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            logging.error(str(exc_val), exc_info=exc_val)
        self.running = False
        self.thread.join(timeout=10)
        if self.thread.is_alive():
            logging.warning(f"thread failed to stop ({self.thread})")

    def __iter__(self):
        yield from self.members

    def run(self):
        self.running = True
        while self.running:
            try:
                self.iteration()
            except Exception as exc:
                logging.error(str(exc), exc_info=exc)
            finally:
                time.sleep(10)

    def iteration(self):
        self.broadcast({'command': "ping"})
        self.listen()

    def broadcast(self, message):
        address = ("255.255.255.255", PORT)
        data = MessageHandler.encryptMessage(message)
        nbytes = self.socket.sendto(data, address)
        logging.debug(f"Send some bytes {nbytes} of {len(data)}")

    def listen(self):
        ka = self.socket.accept()
        print(ka)

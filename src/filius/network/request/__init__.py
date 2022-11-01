#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from functools import cached_property
import socket
from ..message_handler import MessageHandler


class Request:
    def __init__(self, message):
        self.message = message

    @property
    def blob(self):
        return MessageHandler.encryptMessage(self.message)

    def make(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Response:
    def __init__(self, raw: bytes, address: tuple):
        self._raw = raw
        self.address = address

    @cached_property
    def host(self):
        # (name, aliaslist, addresslist)
        return socket.gethostbyaddr(self.ip)

    @cached_property
    def hostname(self):
        return self.host[0]

    @property
    def ip(self):
        return self.address[0]

    @property
    def port(self):
        return self.address[1]

    @cached_property
    def message(self):
        return MessageHandler.decryptData(self._raw)


def get(message) -> Response:
    pass


def getAll(message) -> [Response]:
    pass

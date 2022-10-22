#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import socket
import utility
import marshal
from .. import crypto


PORT = utility.getConfig('port')


class NetClient:
    def __init__(self):
        self.client = socket.create_connection(("", PORT))

    def __getattr__(self, item):
        pass

    def send(self, body):
        self.send_raw()

    def send_raw(self, msg: bytes):
        self.client.sendto(msg, ("255.255.255.255", PORT))

#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import socket
import utility


class NetServer:
    def __init__(self):
        self.server = socket.create_server(("", utility.getConfig('port')))

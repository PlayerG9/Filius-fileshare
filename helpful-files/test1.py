#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import socket


interfaces = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)
print(interfaces)

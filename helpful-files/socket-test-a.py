#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('0.0.0.0', 8080))

while True:
    got = sock.recvfrom(2048)
    print(got)

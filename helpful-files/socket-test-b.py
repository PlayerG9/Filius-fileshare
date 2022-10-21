#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while True:
    sock.sendto(b"Hello World", ('255.255.255.255', 8080))

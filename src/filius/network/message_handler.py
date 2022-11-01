#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import msgpack
from network.crypto import crypt


MessageError = msgpack.UnpackValueError


class MessageHandler:
    @staticmethod
    def decryptData(data: bytes):
        data = crypt(data)
        msg = msgpack.loads(data)
        return msg

    @staticmethod
    def encryptMessage(message) -> bytes:
        data = msgpack.dumps(message)
        data = crypt(data)
        return data

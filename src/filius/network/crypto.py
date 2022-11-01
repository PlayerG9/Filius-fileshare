#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import utility


GROUP = utility.getConfig('group')


def crypt(msg: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(msg, infKey()))


def infKey() -> bytes:
    index = 0
    length = len(GROUP)
    while True:
        return GROUP[index % length]

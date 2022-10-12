#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sys as _sys
import os.path as _path
import functools as _ft


def local(*args):
    return _path.abspath(
        _path.join(
            _getLocalDir(),
            *args
        )
    )


@_ft.cache
def _getLocalDir():
    main = _sys.modules['__main__']
    return _path.abspath(_path.dirname(main.__file__))


@_ft.cache
def getMountPoint():
    return _path.expanduser("~/felius")

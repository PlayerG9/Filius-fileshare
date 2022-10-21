#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sys as _sys
import os.path as _path
import functools as _ft
import subprocess as _sp


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
    from .config import getConfig
    mount = getConfig('mount', default="~/felius")
    return _path.abspath(_path.expanduser(mount))


def openFolderInExplorer(path: str, important: bool = False):
    if _sys.platform == 'darwin':
        _sp.check_call(['open', '--', path])
    elif _sys.platform == 'linux':
        _sp.check_call(['xdg-open', path])
    elif _sys.platform == 'win32':
        _sp.check_call(['explorer', path])
    elif important:
        raise OSError('os is not supported')

#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sys as _sys
import os.path as _path
import functools as _ft
import subprocess as _sp


def sourceFile(*args):
    return _path.abspath(
        _path.join(
            _getSourceDirectory(),
            *args
        )
    )


@_ft.cache
def _getSourceDirectory():
    main = _sys.modules['__main__']
    return _path.abspath(_path.dirname(main.__file__))


def filiusFile(path: str):
    return _path.abspath(
        _path.join(
            getLocalFiliusDirectory(),
            path.lstrip(_path.sep)
        )
    )


@_ft.cache
def getLocalFiliusDirectory():
    return _path.abspath(
        _path.expanduser("~/.filius/files")
    )


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

#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
from . import request_handler


handler = request_handler.RequestHandler()


@handler.register()
def ping():
    return {"message": "pong"}


@handler.register()
@handler.toFiliusPath(0, required=True)
def chmod(path, mode):
    os.chmod(path=path, mode=mode)


@handler.register()
@handler.toFiliusPath(0, required=True)
def chown(path, uid, gid):
    os.chown(path=path, uid=uid, gid=gid)


@handler.register()
@handler.toFiliusPath(0, required=True)
def getxattr(path, name, _position=0):
    return os.getxattr(path=path, attribute=name)


@handler.register()
@handler.toFiliusPath(0, required=True)
def listxattr(path):
    return os.listdir(path=path)


@handler.register()
@handler.toFiliusPath(0, required=True)
def mkdir(path, mode):
    os.mkdir(path=path, mode=mode)


@handler.register()
@handler.toFiliusPath(0, required=True)
def read(path, size, offset, _fh):
    with open(path, 'rb') as file:
        file.seek(offset)
        return file.read(size)


@handler.register()
@handler.toFiliusPath(0, required=True)
def readdir(path, _fh):
    """
    Can return either a list of names, or a list of (name, attrs, offset)
    tuples. attrs is a dict as in getattr.
    """

    return [".", ".."] + os.listdir(path=path)


@handler.register()
@handler.toFiliusPath(0, required=True)
def removexattr(path, name):
    os.removexattr(path=path, attribute=name)


@handler.register()
@handler.toFiliusPath(0, required=True)
@handler.toFiliusPath(1, required=False)
def rename(old, new):
    os.rename(src=old, dst=new)


@handler.register()
@handler.toFiliusPath(0, required=True)
def rmdir(path):
    os.rmdir(path=path)


@handler.register()
@handler.toFiliusPath(0, required=True)
def setxattr(path, name, value, options, _position=0):
    os.setxattr(path=path, attribute=name, value=value, flags=options)


@handler.register()
@handler.toFiliusPath(0, required=True)
def statfs(path):
    """
    Returns a dictionary with keys identical to the statvfs C structure of
    statvfs(3).
    """
    return os.stat(path=path)


@handler.register()
@handler.toFiliusPath(0, required=True)
def truncate(path, length, _fh=None):
    os.truncate(path=path, length=length)


@handler.register()
@handler.toFiliusPath(0, required=True)
def utimens(path, times=None):
    """Times is a (atime, mtime) tuple. If None use current time."""
    os.utime(path=path, times=times)  # maybe ns=times


@handler.register()
@handler.toFiliusPath(0, required=True)  # don't know if required
def write(path, data, offset, _fh):
    with open(path, 'wb') as file:
        file.seek(offset)
        file.write(data)

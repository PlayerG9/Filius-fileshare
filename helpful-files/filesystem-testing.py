#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from refuse.high import FUSE, Operations


class MyOps(Operations):
    def __init__(self):
        self.fd = 0

    def readdir(self, path, fh):
        print(path, fh, type(fh))
        return ['.', '..']

    def create(self, path, mode, fi=None):
        print([path, mode, fi])
        self.fd += 1
        return self.fd

    def open(self, path, flags):
        print([path, flags])
        self.fd += 1
        return self.fd

    def write(self, path, data, offset, fh):
        print([path, data, offset, fh])


if __name__ == '__main__':
    FUSE(MyOps(), '/home/playerg9/filius', foreground=True,)

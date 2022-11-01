#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import utility
import os


class MountPoint:
    def __init__(self):
        self.fileDirectory = utility.getLocalFiliusDirectory()
        self.mount = utility.getMountPoint()
        self.permanent = utility.getConfig('permanent', default=False)

    def __enter__(self):
        # wipe it clean
        if os.path.exists(self.fileDirectory):
            os.rmdir(self.fileDirectory)
        os.makedirs(self.fileDirectory, exist_ok=True)
        os.makedirs(self.mount, exist_ok=True)
        return self.mount

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.rmdir(self.fileDirectory)
        if not self.permanent:
            if os.path.isdir(self.mount):
                os.remove(self.mount)

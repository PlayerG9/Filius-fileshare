#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import utility
import os


class MountPoint:
    def __init__(self):
        self.mount = utility.getMountPoint()
        self.permanent = utility.getConfig('permanent', default=False)

    def __enter__(self):
        os.makedirs(self.mount, exist_ok=True)
        return self.mount

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.permanent:
            if os.path.isdir(self.mount):
                os.remove(self.mount)

#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import socket
import stat
import errno
import refuse.high as fuse
from refuse.high import FuseOSError
from network.netconnector import NetConnector


class FeliusOperations(fuse.Operations):
    """
    When in doubt of what an operation should do, check the FUSE header file
    or the corresponding system call man page.
    """
    def __init__(self):
        self.network = NetConnector()

    def __enter__(self):
        self.network.join()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            logging.error(str(exc_val), exc_info=exc_val)
        self.network.leave()

    def init(self, path):
        """
        Called on filesystem initialization. (Path is always /)

        Use it instead of __init__ if you start threads on initialization.
        """

        pass

    def destroy(self, path):
        """Called on filesystem destruction. Path is always /"""

        pass

    def __call__(self, op, *args):
        print([op, args])
        if not hasattr(self, op):
            raise FuseOSError(errno.EFAULT)
        return getattr(self, op)(*args)

    # def access(self, path, amode):
    #     return 0

    bmap = None

    def chmod(self, path, mode):
        raise FuseOSError(errno.EROFS)

    def chown(self, path, uid, gid):
        raise FuseOSError(errno.EROFS)

    def create(self, path, mode, fi=None):
        """
        When raw_fi is False (default case), fi is None and create should
        return a numerical file handle.

        When raw_fi is True the file handle should be set directly by create
        and return 0.
        """

        raise FuseOSError(errno.EROFS)

    # def flush(self, path, fh):
    #     return 0

    # def fsync(self, path, datasync, fh):
    #     return 0

    # def fsyncdir(self, path, datasync, fh):
    #     return 0

    def getattr(self, path, fh=None):
        """
        Returns a dictionary with keys identical to the stat C structure of
        stat(2).

        st_atime, st_mtime and st_ctime should be floats.

        NOTE: There is an incompatibility between Linux and Mac OS X
        concerning st_nlink of directories. Mac OS X counts all files inside
        the directory, while Linux counts only the subdirectories.
        """

        if path != "/":
            raise FuseOSError(errno.ENOENT)
        return dict(st_mode=(stat.S_IFDIR | 0o755), st_nlink=2)

    def getxattr(self, path, name, position=0):
        raise FuseOSError(errno.ENOTSUP)

    # def ioctl(self, path, cmd, arg, fip, flags, data):
    #     raise FuseOSError(errno.ENOTTY)

    # def link(self, target, source):
    #     """creates a hard link `target -> source` (e.g. ln source target)"""
    #
    #     raise FuseOSError(errno.EROFS)

    def listxattr(self, path):
        return []

    lock = None

    def mkdir(self, path, mode):
        raise FuseOSError(errno.EROFS)

    # def mknod(self, path, mode, dev):
    #     raise FuseOSError(errno.EROFS)

    # def open(self, path, flags):
    #     """
    #     When raw_fi is False (default case), open should return a numerical
    #     file handle.
    #
    #     When raw_fi is True the signature of open becomes:
    #         open(self, path, fi)
    #
    #     and the file handle should be set directly.
    #     """
    #
    #     return 0

    # def opendir(self, path):
    #     """Returns a numerical file handle."""
    #
    #     return 0

    def read(self, path, size, offset, fh):
        """Returns a string containing the data requested."""

        raise FuseOSError(errno.EIO)

    def readdir(self, path, fh):
        """
        Can return either a list of names, or a list of (name, attrs, offset)
        tuples. attrs is a dict as in getattr.
        """
        content = [".", ".."]

        if path == "/":
            content.append("filius-members")

        if path == "/filius-members":
            content.append(socket.gethostname())

        return content

    def readlink(self, path):
        raise FuseOSError(errno.ENOENT)

    # def release(self, path, fh):
    #     return 0

    # def releasedir(self, path, fh):
    #     return 0

    def removexattr(self, path, name):
        raise FuseOSError(errno.ENOTSUP)

    def rename(self, old, new):
        raise FuseOSError(errno.EROFS)

    def rmdir(self, path):
        raise FuseOSError(errno.EROFS)

    def setxattr(self, path, name, value, options, position=0):
        raise FuseOSError(errno.ENOTSUP)

    def statfs(self, path):
        """
        Returns a dictionary with keys identical to the statvfs C structure of
        statvfs(3).

        On Mac OS X f_bsize and f_frsize must be a power of 2
        (minimum 512).
        """

        return {}

    def symlink(self, target, source):
        """creates a symlink `target -> source` (e.g. ln -s source target)"""

        raise FuseOSError(errno.EROFS)

    def truncate(self, path, length, fh=None):
        raise FuseOSError(errno.EROFS)

    def unlink(self, path):
        raise FuseOSError(errno.EROFS)

    def utimens(self, path, times=None):
        """Times is a (atime, mtime) tuple. If None use current time."""

        return 0

    def write(self, path, data, offset, fh):
        raise FuseOSError(errno.EROFS)

#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import application_setup


def main():
    from filesystem import fuse, FeliusOperations
    from filesystem.mountpoint import MountPoint

    with MountPoint() as mount:
        fuse.FUSE(
            operations=FeliusOperations(),
            mountpoint=mount,
            foreground=True,
            # nothreads=True,
        )


if __name__ == '__main__':
    application_setup.run()
    main()

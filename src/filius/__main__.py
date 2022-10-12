#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import application_setup
import utility


def main():
    from filesystem import fuse, Felius

    # with socket-stuff
    with None:
        fuse.FUSE(
            operations=Felius(),
            mountpoint=utility.getMountPoint(),
            foreground=True,
            # nothreads=True,
        )


if __name__ == '__main__':
    application_setup.run()
    main()

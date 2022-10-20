#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import application_setup
import utility


class FakeWith:
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...


def main():
    from filesystem import fuse, Felius

    # with socket-stuff
    with FakeWith():
        fuse.FUSE(
            operations=Felius(),
            mountpoint=utility.getMountPoint(),
            foreground=True,
            # nothreads=True,
        )


if __name__ == '__main__':
    application_setup.run()
    main()

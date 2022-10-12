#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from . import logging_setup
from . import package_setup


def run():
    logging_setup.run()
    package_setup.run()

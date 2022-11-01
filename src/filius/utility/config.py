#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import functools as _ft
from . import paths


def getConfig(*keys, default=...):
    var = loadConfig()

    for key in keys:
        try:
            var = var[key]
        except (KeyError, IndexError, TypeError) as error:
            if isinstance(default, ...):
                raise error
            else:
                return default

    return var


@_ft.cache
def loadConfig() -> dict:
    import json
    with open(paths.sourceFile('config.json'), 'r') as file:
        return json.load(file)

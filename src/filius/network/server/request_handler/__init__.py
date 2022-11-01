#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import functools
import types
from utility import filiusFile as _toLocalPath


class UnknownRequest(Exception):
    pass


class IgnoreRequest(Exception):
    pass


class RequestHandler:
    def __init__(self):
        self._handlers = {}

    def register(self, function: types.FunctionType = None):
        if function is None:
            return self.register
        else:
            self._handlers[function.__name__] = function

    def __call__(self, message: dict):
        command: str = message.get('command').replace('-', '_')
        args: list = message.get('args')
        kwargs: dict = message.get('kwargs')

        handle = self._handlers.get(command, None)

        return handle(*args, **kwargs)

    @staticmethod
    def toFiliusPath(index, required: bool):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                args = list(args)
                if isinstance(index, int):
                    path = args[index] = _toLocalPath(args[index])
                elif isinstance(index, str):
                    path = kwargs[index] = _toLocalPath(kwargs[index])
                else:
                    raise TypeError()

                if required and not os.path.exists(path):
                    raise IgnoreRequest()

                func(*args, **kwargs)

            return wrapper

        return decorator

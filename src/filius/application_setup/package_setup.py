#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import subprocess
import sys
import utility


def run():
    with open(utility.local('package-list.txt'), 'r') as file:
        for line in file:
            if not line.strip():
                continue

            module, package = line.split(',', 1)

            verifyOrInstallModule(module, package)


def verifyOrInstallModule(module: str, packageName: str):
    if moduleExists(module):
        return
    installPackage(packageName)
    if not moduleExists(module):
        raise ModuleNotFoundError(f"Failed to locate or install module: {module!r}")


def moduleExists(module: str) -> bool:
    try:
        __import__(module)
    except ModuleNotFoundError:
        return False
    else:
        return True


def installPackage(packageName: str):
    subprocess.run([sys.executable, '-m', 'pip', 'install', packageName], check=True)

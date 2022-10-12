# filius-fileshare
Decentralised filesharing in the local network

> This Project is currently under development is not usable yet

> This Program is currently developed for Linux based systems  
> Windows may be supported later on

# How does it work

Other users have access to the files you marked as shared

![](README.assets/how-does-it-work.jpg)

# Installation and running

## Installation

```commandline
user@PC:~$ git clone https://github.com/PlayerG9/filius-fileshare.git
user@PC:~$ ./filius-fileshare/scripts/setup
```

## Running

```commandline
user@PC:~$ /path/to/filis-fileshare/filius
```

# Technical Stuff

## File-System
[refuse](https://github.com/pleiszenburg/refuse) is a Python module implemented using [`ctypes`](https://docs.python.org/3/library/ctypes.html) that provides a simple cross-platform interface to:

- [libfuse](https://github.com/libfuse/libfuse)
- [FUSE for macOS](https://osxfuse.github.io/)
- [WinFsp](https://github.com/billziss-gh/winfsp)

# Communication

is based on the python socket library in combination with the [msgpack](https://msgpack.org/) package

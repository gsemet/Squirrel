from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import signal
import sys

from squirrel.common.i18n import setupI18n
from squirrel.common.logging import setupLogger
from squirrel.services.config import dumpConfigToLogger
from squirrel.services.config import initializeConfig
from squirrel.services.config import unloadConfig
from squirrel.services.crawlers import configureCrawlers
from squirrel.services.db import connectDatabase
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins
from squirrel.services.serve_backend import quitBackend


def installTrap():
    def terminate_handler(signum, frame):
        print('Signal handler called with signal', signum)
        quitBackend()
        sys.exit(0)

    def kill_handler(signum, frame):
        print('Signal handler called with signal', signum)
        quitBackend()
        sys.exit(1)

    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGTERM, terminate_handler)
    signal.signal(signal.SIGINT, kill_handler)
    if hasattr(signal, "SIGBREAK"):
        signal.signal(signal.SIGBREAK, terminate_handler)

from ctypes import WINFUNCTYPE
from ctypes import windll
from ctypes.wintypes import BOOL
from ctypes.wintypes import DWORD


# https://github.com/zeromq/pyzmq/pull/559/files
def install_handler_win32():
    if not sys.platform.startswith("win32"):
        return

    kernel32 = windll.LoadLibrary('kernel32')
    PHANDLER_ROUTINE = WINFUNCTYPE(BOOL, DWORD)
    SetConsoleCtrlHandler = kernel32.SetConsoleCtrlHandler
    SetConsoleCtrlHandler.argtypes = (PHANDLER_ROUTINE, BOOL)
    SetConsoleCtrlHandler.restype = BOOL

    CTRL_C_EVENT = 0

    @PHANDLER_ROUTINE
    def console_handler(ctrl_type):
        print("Console handler", ctrl_type)
        if ctrl_type == CTRL_C_EVENT:
            print('ctrl + c')
        return False

    if not SetConsoleCtrlHandler(console_handler, True):
        raise RuntimeError('SetConsoleCtrlHandler failed.')


def serverSetup(prod=False):
    installTrap()
    initializeConfig()
    setupLogger()
    dumpConfigToLogger()
    setupI18n()
    loadPlugins()
    connectDatabase()
    configureCrawlers()


def serverStop():
    unloadConfig()
    unloadPlugins()

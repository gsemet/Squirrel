from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from squirrel.launcher.common import install_handler_win32
from squirrel.launcher.common import serverSetup
from squirrel.launcher.common import serverStop
from squirrel.services.serve_backend import quitBackend
from squirrel.services.serve_backend import serveBackend


def run():
    try:
        install_handler_win32()
        serverSetup()
        serveBackend(serveFrontEnd=False, prod=False)
        serverStop()
    except KeyboardInterrupt:
        print("Ctrl-c pressed ...")
        quitBackend()
        sys.exit(1)

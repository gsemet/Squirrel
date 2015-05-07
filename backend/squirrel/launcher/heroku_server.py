from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from squirrel.launcher.common import serverSetup
from squirrel.launcher.common import serverStop
from squirrel.services.serve_backend import quitBackend
from squirrel.services.serve_backend import serveBackend


def run():

    try:
        serverSetup(flavour="heroku")
        serveBackend(serveFrontEnd=True)
        serverStop()
    except KeyboardInterrupt:
        print("Ctrl-c pressed ...")
        quitBackend()
        sys.exit(1)

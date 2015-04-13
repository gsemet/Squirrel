from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from squirrel.launcher.common import serverSetup
from squirrel.launcher.common import serverStop
from squirrel.services.serve_backend import serveBackend


def run():

    serverSetup()

    serveBackend(serveFrontEnd=True, prod=True)

    serverStop()

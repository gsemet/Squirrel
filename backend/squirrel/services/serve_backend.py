from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os

from twisted.internet import reactor

from squirrel.routes import app
from squirrel.services.config import Config

# Keep this import group bellow the main "from squirrel" import group
from squirrel.routes import *


log = logging.getLogger(__name__)


def findPortNumber():
    port = Config().frontend.port
    if isinstance(port, basestring) and port.startswith("$"):
        env_var_name = port.replace('$', "")
        port = int(os.environ[env_var_name])
    else:
        port = int(port)
    return port


def serveBackend():
    port = findPortNumber()
    log.info("Starging web service on port {!r}".format(port))
    log.info("Serving front end located at: {}".format(Config().frontend.root_fullpath))
    app.run("0.0.0.0", port)


def quitBackend():
    print("Quitting main reactor")
    reactor.callLater(0, reactor.stop)

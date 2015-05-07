from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os

from dictns import Namespace
from twisted.internet import reactor

from squirrel.routes import app
from squirrel.services.config import Config

# Keep this import group bellow the main "from squirrel" import group
from squirrel.routes import *


log = logging.getLogger(__name__)


def serveBackend(serveFrontEnd=True, prod=False, heroku=False):
    if heroku:
        port = int(os.environ['PORT'])
        log.info("Starging web service on {!r} (heroku)".format(port))
    elif prod:
        port = int(Config().frontend.prod_port)
        log.info("Starging web service on {!r} (prod)".format(port))
    else:
        port = int(Config().frontend.dev_port)
        log.info("Starging web service on {!r} (dev)".format(port))
    log.info("Serving front end located at: {}".format(Config().frontend.root_full_path))
    Config().runtime = Namespace()
    Config().runtime.serveFrontEnd = True
    app.run("localhost", port)


def quitBackend():
    print("Quitting main reactor")
    reactor.callLater(0, reactor.stop)

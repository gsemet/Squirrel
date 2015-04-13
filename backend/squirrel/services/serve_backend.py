from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from dictns import Namespace

from squirrel.routes import app
from squirrel.services.config import Config

# Keep this import group bellow the main "from squirrel" import group
from squirrel.routes import *


log = logging.getLogger(__name__)


def serveBackend(serveFrontEnd=True, prod=False):
    if prod:
        port = Config().frontend.prod_port
        log.info("Starging web service on {} (prod)".format(port))
    else:
        port = Config().frontend.dev_port
        log.info("Starging web service on {} (dev)".format(port))
    log.info("Serving front end located at: {}".format(Config().frontend.root_full_path))
    Config().runtime = Namespace()
    Config().runtime.serveFrontEnd = True
    app.run("localhost", port)

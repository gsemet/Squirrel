from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from dictns import Namespace

from squirrel.config.config import Config
from squirrel.routes import app

# Keep this import group bellow the main "from squirrel" import group
from squirrel.routes import *


log = logging.getLogger(__name__)


def serveBackend(serveFrontEnd=True):
    port = Config().frontend.port
    log.info("Starging web service on {}".format(port))
    log.info("Serving front end located at: {}".format(Config().frontend.root_full_path))
    Config().runtime = Namespace()
    Config().runtime.serveFrontEnd = True
    app.run("localhost", port)

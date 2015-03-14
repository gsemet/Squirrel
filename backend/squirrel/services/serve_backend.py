from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from squirrel.config.config import Config
from squirrel.routes import app

from squirrel.routes import *


log = logging.getLogger(__name__)


def serveBackend():
    port = Config().frontend.port
    log.info("Starging web service on {}".format(port))
    log.info("Serving front end located at: {}".format(Config().frontend.root_full_path))
    app.run("localhost", port)

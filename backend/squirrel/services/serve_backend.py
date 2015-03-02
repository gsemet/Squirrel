from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.config.config import Config
from squirrel.routes import app

from squirrel.routes import *


def serveBackend():
    port = Config().frontend.port
    print("Starging web service on {}".format(port))
    print("Serving front end located at: {}".format(Config().frontend.root_full_path))
    app.run("localhost", port)

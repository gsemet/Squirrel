from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import logging

from squirrel.routes import app
from squirrel.services.config import Config

log = logging.getLogger(__name__)


@app.route("/api/flavour", methods=['GET'])
def route_flavour(request):
    request.setHeader('Content-Type', 'application/json')

    return json.dumps(Config().flavour.name)

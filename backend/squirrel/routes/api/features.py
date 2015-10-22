# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging

from squirrel.routes import app
from squirrel.services.config import Config

log = logging.getLogger(__name__)


@app.route("/api/features", methods=['GET'])
def route_features(request):
    request.setHeader('Content-Type', 'application/json')

    return json.dumps(Config().features)

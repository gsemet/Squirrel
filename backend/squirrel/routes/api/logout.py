# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from squirrel.routes import app


@app.route("/api/logout", methods=['POST'])
def route_logout_post(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    data = {}

    return json.dumps(data)


@app.route("/api/logout", methods=['OPTIONS'])
def route_logout_options(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

    data = {}

    return json.dumps(data)

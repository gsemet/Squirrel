from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json

from squirrel.routes import app


@app.route("/api/login", methods=['POST'])
def route_login_post(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    data = {"token": "123456"}

    return json.dumps(data)


@app.route("/api/login", methods=['OPTIONS'])
def route_login_options(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

    data = {"token": "123456"}

    return json.dumps(data)

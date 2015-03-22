from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json

from squirrel.routes import app


@app.route("/api/register", methods=['POST'])
def route_register_post(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    data = {"result": "Failure"}

    return json.dumps(data)


@app.route("/api/register", methods=['OPTIONS'])
def route_register_options(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

    data = {"result": "Failure"}

    return json.dumps(data)

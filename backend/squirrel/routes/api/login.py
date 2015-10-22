# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from squirrel.routes import app


def getLoginData():
    return {
        "session_id": "123456",
        "user_id": "987654",
        "first_name": "Gaetan",
        "last_name": "S",
        "email": "email@adress.com",
        "role": "admin",
        "language": "fr",
        "features": {
            "poc": True,
        }
    }


@app.route("/api/login", methods=['POST'])
def route_login_post(request):
    request.setHeader('Content-Type', 'application/json')

    # method called with 2 different type of data
    #   email + password
    # or
    #   session id

    data = getLoginData()

    return json.dumps(data)


@app.route("/api/login", methods=['OPTIONS'])
def route_login_options(request):
    request.setHeader('Content-Type', 'application/json')

    data = getLoginData()

    return json.dumps(data)

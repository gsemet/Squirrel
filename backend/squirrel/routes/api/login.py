from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json

from squirrel.routes import app


def getLoginData():
    return {
        "id": "123456",
        "userId": "987654",
        "first_name": "Gaetan",
        "last_name": "S",
        "email": "email@adress.com",
        "role": "admin",
        "language": "fr",
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

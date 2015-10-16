from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from squirrel.routes import app


def getLoginData():
    return {
        "id": "123456",
        "userId": "987654",
        "userName": "Gaetan",
        "email": "email@adress.com",
        "role": "admin",
        "lang": "fr",
    }


@app.route("/api/profile", methods=['GET'])
def route_profile_post(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    data = getLoginData()

    return json.dumps(data)

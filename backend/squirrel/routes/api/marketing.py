from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import logging

from squirrel.routes import app
from squirrel.services.config import Config

log = logging.getLogger(__name__)


@app.route("/api/marketing", methods=['GET'])
def route_marketing_get(request):
    request.setHeader('Content-Type', 'application/json')

    req = request.args.get('r', [])
    lang = request.args.get('l', ["us"])
    log.info("request received for marketing req={!r}, lang={!r}".format(req, lang))
    if len(req) == 0:
        return json.dumps({})
    req = req.pop(0)
    if len(lang) == 0:
        return json.dumps({})
    lang = lang.pop(0)
    data = {}
    if req == "homepage-accounts":
        data = Config().marketing.country.get(lang, {}).get("homepage_accounts", {})

    return json.dumps(data)

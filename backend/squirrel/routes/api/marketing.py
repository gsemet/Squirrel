# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging

from squirrel.routes import app
from squirrel.routes.api import getSingleArgFromRequest
from squirrel.services.config import Config

log = logging.getLogger(__name__)


@app.route("/api/marketing", methods=['GET'])
def route_marketing_get(request):
    request.setHeader('Content-Type', 'application/json')

    req = getSingleArgFromRequest(request, 'r')
    lang = getSingleArgFromRequest(request, 'l', default="us")
    log.info("request received for marketing req={!r}, lang={!r}".format(req, lang))
    if req is None:
        return json.dumps({})
    if lang is None:
        lang = "us"
    data = {}
    if req == "homepage-accounts":
        data = Config().marketing.country.get(lang, {}).get("homepage_accounts", {})

    return json.dumps(data)

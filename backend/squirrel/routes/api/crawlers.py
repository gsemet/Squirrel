from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.common.json import json
from squirrel.routes import app
from squirrel.services.crawlers import CrawlerConfig


@app.route("/api/crawlers", methods=['GET'])
def route_crawlers_get(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    request.setResponseCode(200)
    data = CrawlerConfig().getAllCrawlerDescriptions()

    return json.dumps(data)

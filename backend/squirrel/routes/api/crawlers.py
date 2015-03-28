from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet import defer

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

ALLOWED_ACTIONS = {'start', 'stop', 'progress'}


@app.route("/api/crawlers/<path:crawler>", methods=['GET'])
@defer.inlineCallbacks
def route_crawlers_action(request, crawler):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    actions = request.args.get('action', [])
    if not actions:
        request.setResponseCode(501)
        defer.returnValue(json.dumps({
                                     'error': 501,
                                     'message': 'no actions'
                                     }))
    action = actions[0]
    if not action or action not in ALLOWED_ACTIONS:
        request.setResponseCode(501)
        defer.returnValue(json.dumps({
                                     "error": 501,
                                     "message": "unallowed action"
                                     }))

    if action == "start":
        yield CrawlerConfig().start(crawler)
        request.setResponseCode(200)
        defer.returnValue(json.dumps({'message': 'request sent.'}))
    elif action == "start":
        yield CrawlerConfig().stop(crawler)
        request.setResponseCode(200)
        defer.returnValue(json.dumps({'message': 'request sent.'}))
    elif action == "progress":
        progr = yield CrawlerConfig().getProgress(crawler)
        request.setResponseCode(200)
        defer.returnValue(json.dumps({'progress': str(progr)}))
    else:
        request.setResponseCode(501)
        defer.returnValue(json.dumps({'error': 'unexpected error!'}))

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from twisted.internet import defer

from squirrel.common.json import json
from squirrel.common.result import EXCEPTION
from squirrel.common.result import SUCCESS
from squirrel.common.result import resultToString
from squirrel.routes import app
from squirrel.routes.api import getSingleArgFromRequest
from squirrel.services.crawlers import CrawlerConfig


@app.route("/api/crawlers", methods=['GET'])
def route_crawlers_get(request):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    request.setResponseCode(SUCCESS)
    data = CrawlerConfig().getAllCrawlerDescriptions()

    return json.dumps(data)

ALLOWED_ACTIONS = {'start', 'stop', 'progress'}


@app.route("/api/crawlers/<path:crawler>", methods=['GET'])
@defer.inlineCallbacks
def route_crawlers_action(request, crawler):
    request.setHeader('Content-Type', 'application/json')
    request.setHeader('Access-Control-Allow-Origin', '*')

    if not request.args:
        (res, message) = CrawlerConfig().getStatus(crawler)
        defer.returnValue(json.dumps({
            'result': resultToString(res),
            'code': res,
            'message': message
        }))

    action = getSingleArgFromRequest(request, 'action')
    if not action:
        request.setResponseCode(EXCEPTION)
        defer.returnValue(json.dumps({
                                     'error': EXCEPTION,
                                     'message': 'no actions'
                                     }))
    if not action or action not in ALLOWED_ACTIONS:
        request.setResponseCode(EXCEPTION)
        defer.returnValue(json.dumps({
                                     "error": EXCEPTION,
                                     "message": "unallowed action"
                                     }))

    if action == "start":
        (res, message) = yield CrawlerConfig().start(crawler)
        request.setResponseCode(res)
        defer.returnValue(json.dumps({
            'result': resultToString(res),
            'code': res,
            'message': message
        }))
    elif action == "stop":
        (res, message) = yield CrawlerConfig().stop(crawler)
        defer.returnValue(json.dumps({
            'result': resultToString(res),
            'code': res,
            'message': message
        }))
    elif action == "progress":
        (res, message) = yield CrawlerConfig().getProgress(crawler)
        defer.returnValue(json.dumps({
            'result': resultToString(res),
            'code': res,
            'message': message
        }))
    else:
        request.setResponseCode(EXCEPTION)
        defer.returnValue(json.dumps({
            'result': 'error',
            'code': EXCEPTION,
            'error': resultToString(EXCEPTION)
        }))

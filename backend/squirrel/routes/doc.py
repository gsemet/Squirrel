# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from twisted.web.util import redirectTo

from squirrel.config.constants import DOC_ENTRY_POINT
from squirrel.config.constants import DOC_INDEX_FILE
from squirrel.routes import app
from squirrel.routes import serve_url
from squirrel.services.config import Config


@app.route(DOC_ENTRY_POINT, methods=['GET'])
def redirect(request):
    return redirectTo(DOC_ENTRY_POINT + '/' + DOC_INDEX_FILE, request)


@app.route(DOC_ENTRY_POINT + '/<path:path1>', methods=['GET'])
def help1(request, path1):
    return serve_url(path1, Config().frontend.doc_fullpath)


@app.route(DOC_ENTRY_POINT + '/<path:path1>/<path:path2>', methods=['GET'])
def help2(request, path1, path2):
    return serve_url(path1 + "/" + path2, Config().frontend.doc_fullpath)


@app.route(DOC_ENTRY_POINT + '/<path:path1>/<path:path2>/<path:path3>', methods=['GET'])
def help3(request, path1, path2, path3):
    return serve_url(path1 + "/" + path2 + "/" + path3, Config().frontend.doc_fullpath)

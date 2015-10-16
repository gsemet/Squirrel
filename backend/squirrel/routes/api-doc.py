from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from squirrel.config.constants import API_DOC_ENTRY_POINT
from squirrel.routes import app
from squirrel.routes import serve_url
from squirrel.services.config import Config


@app.route(API_DOC_ENTRY_POINT + '/<path:path1>', methods=['GET'])
def api_doc1(request, path1):
    return serve_url(path1, Config().frontend.doc_fullpath)


@app.route(API_DOC_ENTRY_POINT + '/<path:path1>/<path:path2>', methods=['GET'])
def api_doc2(request, path1, path2):
    return serve_url(path1 + "/" + path2, Config().frontend.doc_fullpath)


@app.route(API_DOC_ENTRY_POINT + '/<path:path1>/<path:path2>/<path:path3>', methods=['GET'])
def api_doc3(request, path1, path2, path3):
    return serve_url(path1 + "/" + path2 + "/" + path3, Config().frontend.doc_fullpath)


@app.route(API_DOC_ENTRY_POINT + '/<path:path1>/<path:path2>/<path:path3>/<path:path4>',
           methods=['GET'])
def api_doc4(request, path1, path2, path3, path4):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4,
                     Config().frontend.doc_fullpath)


@app.route(API_DOC_ENTRY_POINT + '/<path:path1>/<path:path2>/<path:path3>/<path:path4>/<path:path5>',
           methods=['GET'])
def api_doc5(request, path1, path2, path3, path4, path5):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4 + "/" + path5,
                     Config().frontend.doc_fullpath)


@app.route(API_DOC_ENTRY_POINT +
           '/<path:path1>/<path:path2>/<path:path3>/<path:path4>/<path:path5>/<path:path6>',
           methods=['GET'])
def api_doc6(request, path1, path2, path3, path4, path5, path6):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4 + "/" + path5 + "/" + path6,
                     Config().frontend.doc_fullpath)

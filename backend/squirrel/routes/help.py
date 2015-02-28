from twisted.web.util import redirectTo

from squirrel.config.config import Config
from squirrel.config.constants import DOC_INDEX_FILE
from squirrel.config.constants import HELP_ENTRY_POINT
from squirrel.routes import app
from squirrel.routes import serve_url


@app.route(HELP_ENTRY_POINT, methods=['GET'])
def redirect(request):
    return redirectTo(HELP_ENTRY_POINT + '/' + DOC_INDEX_FILE, request)


@app.route(HELP_ENTRY_POINT + '/<path:path1>', methods=['GET'])
def help1(request, path1):
    return serve_url(path1, Config().frontend['doc_full_path'])


@app.route(HELP_ENTRY_POINT + '/<path:path1>/<path:path2>', methods=['GET'])
def help2(request, path1, path2):
    return serve_url(path1 + "/" + path2, Config().frontend['doc_full_path'])


@app.route(HELP_ENTRY_POINT + '/<path:path1>/<path:path2>/<path:path3>', methods=['GET'])
def help3(request, path1, path2, path3):
    return serve_url(path1 + "/" + path2 + "/" + path3, Config().frontend['doc_full_path'])

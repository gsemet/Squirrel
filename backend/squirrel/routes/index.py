from twisted.web.util import redirectTo

from squirrel.config.config import Config
from squirrel.config.constants import FRONTEND_INDEX_FILE
from squirrel.routes import app
from squirrel.routes import serve_url


@app.route('/<path:path1>', methods=['GET'])
def index1(request, path1):
    return serve_url(path1, Config().frontend['root_full_path'])


@app.route('/<path:path1>/<path:path2>', methods=['GET'])
def index2(request, path1, path2):
    return serve_url(path1 + "/" + path2, Config().frontend['root_full_path'])


@app.route('/<path:path1>/<path:path2>/<path:path3>', methods=['GET'])
def index3(request, path1, path2, path3):
    return serve_url(path1 + "/" + path2 + "/" + path3, Config().frontend['root_full_path'])


@app.route('/<path:path1>/<path:path2>/<path:path3>/<path:path4>', methods=['GET'])
def index4(request, path1, path2, path3, path4):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4,
                     Config().frontend['root_full_path'])


@app.route('/', methods=['GET'], branch=True)
def get_root(request):
    print "request root"
    return redirectTo(FRONTEND_INDEX_FILE, request)

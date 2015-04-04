from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from squirrel.config.constants import FRONTEND_INDEX_FILE
from squirrel.routes import app
from squirrel.routes import serve_url
from squirrel.services.config import Config


log = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def get_root(request):
    log.debug("request root")
    s = serve_url(FRONTEND_INDEX_FILE, Config().frontend.root_full_path)
    # http://stackoverflow.com/questions/22929920/no-such-resource-404-error
    # > Twisted considers a URL at the top level (like your http://localhost:8000) to include an
    # > implicit trailing slash (http://localhost:8000/). That means that the URL path includes an
    # > empty segment. Twisted then looks in the resource for a child named '' (empty string).
    s.putChild('', s)

    request.setHeader("Expires", "Thu, 15 Apr 2010 20:00:00 GMT")
    return s


@app.route('/<path:path1>', methods=['GET'])
def index1(request, path1):
    return serve_url(path1, Config().frontend.root_full_path)


@app.route('/<path:path1>/<path:path2>', methods=['GET'])
def index2(request, path1, path2):
    return serve_url(path1 + "/" + path2, Config().frontend.root_full_path)


@app.route('/<path:path1>/<path:path2>/<path:path3>', methods=['GET'])
def index3(request, path1, path2, path3):
    return serve_url(path1 + "/" + path2 + "/" + path3, Config().frontend.root_full_path)


@app.route('/<path:path1>/<path:path2>/<path:path3>/<path:path4>', methods=['GET'])
def index4(request, path1, path2, path3, path4):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4,
                     Config().frontend.root_full_path)


# localhost:3000/bower_components/bootstrap/fonts/glyphicons-halflings-regular.woff2

@app.route('/<path:path1>/<path:path2>/<path:path3>/<path:path4>/<path:path5>', methods=['GET'])
def index5(request, path1, path2, path3, path4, path5):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4 + "/" + path5,
                     Config().frontend.root_full_path)


@app.route('/<path:path1>/<path:path2>/<path:path3>/<path:path4>/<path:path5>/<path:path6>',
           methods=['GET'])
def index6(request, path1, path2, path3, path4, path5, path6):
    return serve_url(path1 + "/" + path2 + "/" + path3 + "/" + path4 + "/" + path5 + "/" + path6,
                     Config().frontend.root_full_path)

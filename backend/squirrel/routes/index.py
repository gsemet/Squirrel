import os
import sys

from twisted.web.static import File, DirectoryLister
from twisted.web.util import redirectTo

from squirrel.config.config import Config
from squirrel.config.constants import INDEX_FILE, IMG_DIR, STYLES_DIR, SCRIPTS_DIR, FONTS_DIR
from squirrel.routes import app


def serve_file(wanted_url):
    root = Config().frontend['root_full_path']
    print "root: {!r}".format(root)
    if sys.platform == "win32":
        wanted_url = wanted_url.replace("/", "\\")
    print "wanted_url", wanted_url
    full_file_path = os.path.join(root, wanted_url)
    # Seems like twisted DirectoryLister doesn't like unicode input
    # http://stackoverflow.com/questions/20433559/twisted-web-file-directory-listing-issues
    full_file_path = full_file_path.encode('ascii', 'ignore')
    print "Serving url {!r} with file {!r}".format(wanted_url, full_file_path)
    if os.path.isdir(full_file_path):
        print "Dir exists: {}".format(os.path.exists(full_file_path))
        print "should list: os.listdir(self.path)", os.listdir(full_file_path)
        return DirectoryLister(full_file_path)
    print "File exists: {}".format(os.path.exists(full_file_path))
    return File(full_file_path)


@app.route('/<path>', methods=['GET'], branch=True)
def get_path(request, path):
    print "Request received for: ", path
    return serve_file(path)


@app.route('/' + STYLES_DIR + '/<path>', methods=['GET'], branch=True)
def get_style(request, path):
    print "Request received for {}: {}".format(STYLES_DIR, path)
    return serve_file(STYLES_DIR + "/" + path)


@app.route('/' + SCRIPTS_DIR + '/<path>', methods=['GET'], branch=True)
def get_script(request, path):
    print "Request received for {}: {}".format(SCRIPTS_DIR, path)
    return serve_file(SCRIPTS_DIR + "/" + path)


@app.route('/' + FONTS_DIR + '/<path>', methods=['GET'], branch=True)
def get_font(request, path):
    print "Request received for {}: {}".format(FONTS_DIR, path)
    return serve_file(FONTS_DIR + "/" + path)


@app.route('/' + IMG_DIR + '/<path>', methods=['GET'], branch=True)
def get_image(request, path):
    print "Request received for {}: {}".format(IMG_DIR, path)
    return serve_file(IMG_DIR + "/" + path)


@app.route('/', methods=['GET'], branch=True)
def get_root(request):
    print "request root"
    return redirectTo(INDEX_FILE, request)

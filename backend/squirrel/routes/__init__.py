from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import glob
import logging
import os

from klein import Klein
from twisted.web.static import DirectoryLister
from twisted.web.static import File

app = Klein()
log = logging.getLogger(__name__)


def autoroute(python_file, **kwargs):
    current_dir = os.path.dirname(__file__)
    route = python_file.replace(current_dir, "")
    route = route.replace(".pyc", "")
    route = route.replace(".py", "")
    log.debug("route", route)
    return app.route(route, **kwargs)


def serve_url(wanted_url, root_path):
    log.debug("root: {!r}".format(root_path))
    wanted_url = os.path.normpath(wanted_url)
    log.debug("wanted_url", wanted_url)
    full_file_path = os.path.join(root_path, wanted_url)
    # Seems like twisted DirectoryLister doesn't like unicode input
    # http://stackoverflow.com/questions/20433559/twisted-web-file-directory-listing-issues
    full_file_path = full_file_path.encode('ascii', 'ignore')
    log.debug("Serving url {!r} with file {!r}".format(wanted_url, full_file_path))
    if os.path.isdir(full_file_path):
        log.debug("Dir exists: {}".format(os.path.exists(full_file_path)))
        log.debug("should list: os.listdir(self.path)", os.listdir(full_file_path))
        return DirectoryLister(full_file_path)
    log.debug("File exists: {}".format(os.path.exists(full_file_path)))
    return File(full_file_path)


# injecting all *.py file other than __init__.py in this file
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]


from squirrel.routes.api import *

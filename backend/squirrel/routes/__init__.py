from __future__ import absolute_import

import glob
import os

from klein import Klein
from twisted.web.static import DirectoryLister
from twisted.web.static import File

app = Klein()


def autoroute(python_file, **kwargs):
    current_dir = os.path.dirname(__file__)
    route = python_file.replace(current_dir, "")
    route = route.replace(".pyc", "")
    route = route.replace(".py", "")
    print "route", route
    return app.route(route, **kwargs)


def serve_url(wanted_url, root_path):
    print "root: {!r}".format(root_path)
    wanted_url = os.path.normpath(wanted_url)
    print "wanted_url", wanted_url
    full_file_path = os.path.join(root_path, wanted_url)
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


# injecting all *.py file other than __init__.py in this file
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]


from squirrel.routes.api import *

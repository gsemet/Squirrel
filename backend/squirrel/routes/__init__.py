import os
import glob

from klein import Klein
app = Klein()

from squirrel.routes import app


def autoroute(python_file, **kwargs):
    current_dir = os.path.dirname(__file__)
    route = python_file.replace(current_dir, "")
    route = route.replace(".pyc", "")
    route = route.replace(".py", "")
    print "route", route
    return app.route(route, **kwargs)


# injecting all *.py file other than __init__.py in this file
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]


from squirrel.routes.api import *

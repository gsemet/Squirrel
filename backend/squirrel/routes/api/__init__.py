from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import os

# injecting all *.py file other than __init__.py in this file
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]


def getSingleArgFromRequest(request, argKey, default=None):
    if default is not None:
        res = request.args.get(argKey, [default])
    else:
        res = request.args.get(argKey, [])
    if len(res) == 0:
        return None
    else:
        return res.pop(0)


def getMultiArgFromRequest(request, argKey, default=None):
    if default is not None:
        res = request.args.get(argKey, default)
    else:
        res = request.args.get(argKey, [])
    if len(res) == 0:
        return None
    else:
        return res

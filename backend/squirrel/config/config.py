from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from dictns import Namespace
from dictns import _appendToParent

from squirrel.common.singleton import singleton


def _dumpFlat(n, parent=None):
    s = ""
    for k, v in n.items():
        me = _appendToParent(parent, k)

        def do_item(me, v):
            t = type(v).__name__
            if t == "Namespace":
                t = "dict"
            if isinstance(v, dict):
                v = Namespace(v)
                s = _dumpFlat(v, me)
            elif type(v) == list:
                s = me + " = " + str(v) + "\n"
                if len(v) > 0:
                    v = v[0]
                    s += do_item(me + "[i]", v)
            else:
                s = me + " = " + str(v) + "\n"
            return s
        s += do_item(me, v)
    return s


@singleton
class Config(object):

    def __init__(self, *args, **kwargs):
        self.cfg = Namespace(*args, **kwargs)

    def dumpFlat(self, parent=None):
        return _dumpFlat(self)

    def __getattr__(self, name):
        return getattr(self.cfg, name)

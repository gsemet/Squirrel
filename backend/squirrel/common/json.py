from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum
import json as libjson


class EnumEncoder(libjson.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return {
                "__enum__": str(obj)
            }
        return libjson.libjsonEncoder.default(self, obj)


def as_enum(d):
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        return getattr(globals()[name], member)
    else:
        return d


class json(object):

    @staticmethod
    def loads(s):
        return libjson.loads(s, cls=EnumEncoder)

    @staticmethod
    def dumps(s):
        return libjson.dumps(s, cls=EnumEncoder)

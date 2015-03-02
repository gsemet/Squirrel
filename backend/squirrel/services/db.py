from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from twisted.application.service import Service

from squirrel.common.singleton import singleton


def connectDatabase():
    print("Connecting to DB")


@singleton
class Db(Service):
    pass

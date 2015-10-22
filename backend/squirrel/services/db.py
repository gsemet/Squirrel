# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from twisted.application.service import Service

from squirrel.common.singleton import singleton

log = logging.getLogger(__name__)


def connectDatabase():
    log.info("Connecting to DB")


@singleton
class Db(Service):
    pass

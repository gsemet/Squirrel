# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa

from squirrel.common.unittest import TestCase
from squirrel.db.model import Model


class TestPortfolios(TestCase):

    def test1(self):
        model = Model()
        model.start()

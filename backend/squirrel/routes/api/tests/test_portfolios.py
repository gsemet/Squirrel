from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from squirrel.common.unittest import TestCase
from squirrel.routes.api.portfolios import _getAccountTypes
from squirrel.services.config import Config


class TestGetAccountTypes(TestCase):

    def givenListCreatedWith(self, items):
        Config().unload()
        Config({
            'settings': {'country': {'fr': {'asset_types': items}}}
        })

    def executeGetAccountType(self):
        self.c = _getAccountTypes()

    def assertReturnedDataEquals(self, expectedData):
        self.assertEqual(expectedData, self.c)

    def testEmptySettings(self):
        self.givenListCreatedWith({})
        self.executeGetAccountType()
        self.assertReturnedDataEquals([])

    def testTwoUnderedGroups(self):
        self.givenListCreatedWith({
            'type1': [
                't1item2',
                't1item1',
                't1item3',
            ],
            'type2': [
                't2item3',
                't2item2',
                't2item1',
            ],
        })
        self.executeGetAccountType()
        self.assertReturnedDataEquals([
            ('type1', 't1item1'),
            ('type1', 't1item2'),
            ('type1', 't1item3'),
            ('type2', 't2item1'),
            ('type2', 't2item2'),
            ('type2', 't2item3')
        ])

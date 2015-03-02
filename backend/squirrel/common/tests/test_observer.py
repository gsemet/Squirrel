from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.common.observer import Observer
from squirrel.common.unittest import TestCase


class TestObserver(TestCase):

    def testObserver(self):
        # Example usage
        class Data(Observer):

            def __init__(self, name=''):
                super(Data, self).__init__()
                self.name = name
                self._data = 0

            @property
            def data(self):
                return self._data

            @data.setter
            def data(self, value):
                self._data = value
                self.notify()

        class HexViewer(object):

            data = None

            def update(self, subject):
                self.data = hex(subject.data)[2:]

        class DecimalViewer(object):

            data = None

            def update(self, subject):
                self.data = subject.data

        data1 = Data('Data 1')
        viewDec = DecimalViewer()
        viewHex = HexViewer()
        data1.attach(viewDec)
        data1.attach(viewHex)

        # Setting Data 1 = 10
        data1.data = 10

        self.assertEqual(viewHex.data, "a")
        self.assertEqual(viewDec.data, 10)

        # Setting Data 1 = 3
        data1.data = 3

        self.assertEqual(viewHex.data, "3")
        self.assertEqual(viewDec.data, 3)

        # Detach HexViewer from data1 and data2.
        data1.detach(viewHex)
        # Setting Data 1 = 10
        data1.data = 10

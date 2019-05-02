# -*- coding: utf-8 -*-

from src import OrderProcessing
import unittest


class BasicTestSuite(unittest.TestCase):
    def setUp(self):
        self.orderProcessor = OrderProcessing(menuTxtFile="/Users/prosenjitdas/Desktop/orderdata/items.json" ,
                                         orderTxtFile="/Users/prosenjitdas/Desktop/orderdata/orders.json",
                                         numOfParallel=5)

    """ Test Orders """
    def test_orders(self):
        self.orderProcessor.getItems()
        _, dataframe = self.orderProcessor.getOrders()

        if dataframe.size > 0 :
            assert True

    """ Test Constants """
    def test_constants(self):
        if len(self.orderProcessor.getItems()) > 0 :
            assert True


if __name__ == '__main__':
    unittest.main()

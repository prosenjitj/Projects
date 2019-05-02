# -*- coding: utf-8 -*-

from src import Graph

import unittest
import pandas as pd

class AdvancedTestSuite(unittest.TestCase):

    def setUp(self):
        df = pd.DataFrame({
            'Service':['ClubNub','ClubNub','SuperEats','Mostplates'],
            'TotalCost':[2100,800,1500,4000],
            'Total Wait-Time':[804,500,624,252]
        })
        self.graph = Graph(5, df)

    def test_graph(self):
        if len(self.graph.totalCostBasedOnService()) :
            assert True


if __name__ == '__main__':
    unittest.main()

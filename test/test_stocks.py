import pandas as pd
from oilhighfreqfundy import stocks
import unittest


class TestMP(unittest.TestCase):

    def test_ara(self):
        res = stocks.ara_stocks(start_date='2020-01-01')
        self.assertIn('STK-JET-ARA', res.columns)

    def test_sing(self):
        res = stocks.sing_stocks(start_date='2020-01-01')
        self.assertIn('STKLD-SIN', res.columns)

    def test_fuj(self):
        res = stocks.sing_stocks(start_date='2020-01-01')
        self.assertIn('FUJMD04', res.columns)

if __name__ == '__main__':
    unittest.main()
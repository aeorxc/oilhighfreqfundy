from oilhighfreqfundy import stocks
import unittest


class TestMP(unittest.TestCase):

    def test_eia(self):
        res = stocks.eia_stocks()
        self.assertIn('PET.WCESTUS1.W', res.columns)

    def test_ara(self):
        res = stocks.ara_stocks(start_date='2020-01-01')
        self.assertIn('STK-JET-ARA', res.columns)

    def test_sing(self):
        res = stocks.sing_stocks(start_date='2020-01-01')
        self.assertIn('STKLD-SIN', res.columns)

    def test_fuj(self):
        res = stocks.fuj_stocks(start_date='2020-01-01')
        self.assertIn('FUJMD04', res.columns)


if __name__ == '__main__':
    unittest.main()
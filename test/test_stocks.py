from oilhighfreqfundy import stocks
import unittest
import pandas as pd


class TestMP(unittest.TestCase):

    def test_eia(self):
        res = stocks.eia_stocks()
        self.assertIn('PET.WCESTUS1.W', res.columns)

    def test_ara(self):
        res = stocks.ara_stocks(start_date='2020-01-01')
        self.assertIn('STK-JET-ARA', res.columns)
        # Not freq might not be consistent across time, so this won't be true across history
        self.assertEqual(pd.infer_freq(res.index), 'W-THU')

    def test_sing(self):
        res = stocks.sing_stocks(start_date='2020-01-01')
        self.assertIn('STKLD-SIN', res.columns)
        self.assertEqual(pd.infer_freq(res.index), 'W-WED')

    def test_fuj(self):
        res = stocks.fuj_stocks(start_date='2020-01-01')
        self.assertIn('FUJMD04', res.columns)

    def test_eia_bullish_bearish(self):
        # build bigger than expected
        res = stocks.eia_bullish_bearish(1, 0.5)
        self.assertEqual('Bearish', res)
        # build smaller than expected
        res = stocks.eia_bullish_bearish(1, 1.5)
        self.assertEqual('Bullish', res)

        # draw bigger than expected
        res = stocks.eia_bullish_bearish(-1, -0.5)
        self.assertEqual('Bullish', res)
        # draw smaller than expected
        res = stocks.eia_bullish_bearish(-1, -1.5)
        self.assertEqual('Bearish', res)



if __name__ == '__main__':
    unittest.main()
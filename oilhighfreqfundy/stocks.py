import pandas as pd
import eikon as ek
import os
import urllib
import json
from oilhighfreqfundy import symbols

eikonkey = os.environ['EIKON_KEY']
ek.set_app_key(eikonkey)

eia_api_key = os.environ['EIA_KEY']
eia_series_url = 'http://api.eia.gov/series/?api_key={}&series_id={}'

start_date = '2010-01-01'


def ara_stocks(start_date=start_date):
    # note crude is from Genscape but is a subscription: 0#GNS-ARC-STOR
    rics = ['STK-GL-ARA', 'STK-NAF-ARA', 'STK-GO-ARA', 'STK-FO-ARA', 'STK-JET-ARA']
    df = ek.get_timeseries(rics, fields='Close', start_date=start_date)
    return df


def sing_stocks(start_date=start_date):
    rics = ['STKLD-SIN', 'STKMD-SIN', 'STKRS-SIN']
    df = ek.get_timeseries(rics, fields='Close', start_date=start_date)
    return df


def fuj_stocks(start_date=start_date):
    rics = ['FUJLD04', 'FUJMD04', 'FUJHD04']
    df = ek.get_timeseries(rics, fields='Close', start_date=start_date)
    return df


def eia_stocks():
    # symbols from
    # http://ir.eia.gov/wpsr/psw01.xls
    # http://ir.eia.gov/wpsr/psw04.xls

    u = eia_series_url.format(eia_api_key, ';'.join(list(symbols.eia_symbols.keys())))
    contents = urllib.request.urlopen(u)
    j = json.load(contents)
    dfs = []
    if 'series' in j:
        for series in j['series']:
            d = pd.DataFrame(series['data'], columns=['Date', series['series_id']]).set_index('Date')
            d.index = pd.to_datetime(d.index)
            dfs.append(d)
        df = pd.concat(dfs, 1)

        return df


def eia_release_analysis():
    """
    Determine if stocks are bullish/bearish relative to Reuters poll
    :return:
    """

    d = ek.get_data(['USOILC=ECI', 'USOILG=ECI', 'USOILD=ECI'], fields=['CTBTR_1', 'RTR_POLL'])
    d = d[0]
    d = d.rename(columns={'CTBTR_1': 'Actual', 'RTR_POLL': 'Expected'})
    d = d.replace({'USOILC=ECI': 'Crude', 'USOILG=ECI': 'Gas', 'USOILD=ECI': 'Distillate'})
    d['Direction'] = d.apply(lambda x: eia_bullish_bearish(x.Actual, x.Expected), 1)

    return d


def eia_bullish_bearish(actual, expected):
    if pd.isnull(expected):
        return ''

    v = 'Neutral'
    if actual > 0:
        v = 'Bearish'
    else:
        v = 'Bullish'

    if not pd.isnull(expected):
        diff = actual - expected
        if diff >= -0.25 and diff <= 0.25 : # is within 250kb of poll, mark as neutral
            v = 'Neutral'
        if v == 'Bearish' and diff < -0.25:
            v = 'Bullish' # build smaller than expected
        if v == 'Bullish' and diff > 0.25:
            v = 'Bearish' # draw smaller than expected

    return v


def paj_stock():
    # todo
    # https://stats.paj.gr.jp/en/pub/index.html
    # platts code in Reuters AALOL00
    pass


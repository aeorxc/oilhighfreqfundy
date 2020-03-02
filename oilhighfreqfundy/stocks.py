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


def paj_stock():
    # todo
    # https://stats.paj.gr.jp/en/pub/index.html
    # platts code in Reuters AALOL00
    pass


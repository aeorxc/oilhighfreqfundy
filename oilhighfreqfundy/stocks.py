import pandas as pd
import eikon as ek
import os
import urllib
import json

eikonkey = os.environ['EIKON_KEY']
ek.set_app_key(eikonkey)

eia_api_key = os.environ['EIA_KEY']
eia_series_url = 'http://api.eia.gov/series/?api_key={}&series_id={}'

start_date = '2010-01-01'


def ara_stocks(start_date=start_date):
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
    symbols = ['PET.WCRSTUS1.W','PET.WCESTUS1.W','PET.WCSSTUS1.W','PET.WGTSTUS1.W','PET.WGRSTUS1.W','PET.WG4ST_NUS_1.W','PET.WBCSTUS1.W','PET.W_EPOOXE_SAE_NUS_MBBL.W','PET.WKJSTUS1.W','PET.WDISTUS1.W','PET.WD0ST_NUS_1.W','PET.WD1ST_NUS_1.W','PET.WDGSTUS1.W','PET.WRESTUS1.W','PET.WPRSTUS1.W','PET.W_EPPO6_SAE_NUS_MBBL.W','PET.WUOSTUS1.W','PET.WTTSTUS1.W','PET.WTESTUS1.W','PET.WCRSTUS1.W','PET.WCESTUS1.W','PET.WCESTP11.W','PET.WCESTP21.W','PET.W_EPC0_SAX_YCUOK_MBBL.W','PET.WCESTP31.W','PET.WCESTP41.W','PET.WCESTP51.W','PET.W_EPC0_SKA_NUS_MBBL.W','PET.WCSSTUS1.W','PET.WGTSTUS1.W','PET.WGRSTUS1.W','PET.WG4ST_NUS_1.W','PET.WBCSTUS1.W','PET.W_EPOOXE_SAE_NUS_MBBL.W','PET.WKJSTUS1.W','PET.WDISTUS1.W','PET.WD0ST_NUS_1.W','PET.WD1ST_NUS_1.W','PET.WDGSTUS1.W','PET.WRESTUS1.W','PET.WPRSTUS1.W','PET.W_EPPO6_SAE_NUS_MBBL.W','PET.WUOSTUS1.W','PET.WTTSTUS1.W','PET.WTESTUS1.W']

    u = eia_series_url.format(eia_api_key, ';'.join(symbols))
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
import eikon as ek
import os

eikonkey = os.environ['EIKON_KEY']
ek.set_app_key(eikonkey)

eiakey = os.environ['EIA_KEY']


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
    rics = ['FUJLD04', 'FUJMD04' 'FUJHD04']
    df = ek.get_timeseries(rics, fields='Close', start_date=start_date)
    return df


def eia_stocks():
    pass


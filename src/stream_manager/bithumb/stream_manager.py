from datetime import now
from datetime import timedelta

from stream_manager.abstract_stream_manager import AbstractStreamManager
from stream_manager.bithumb.core import PublicApi


class BithumbStreamManager(AbstractStreamManager):
    def __init__(self):
        """
        self.config = {
            'tickers' : {
                'function' : self.get_tickers,
                'kwargs_list' : [{'interval' :timedelta(hours=1)}]
            },
            'orderbooks' :{
                'function' : self.get_orderbooks,
                'kwargs_list' : [{'interval' :timedelta(seconds=5)}]
            },
            'transactions' :{
                'function' : self.get_transaction_history,
                'kwargs_list' : [{'interval':timedelta(seconds=5), 'order_currency':x,} for x in BITHUMB_TICKERS]
            },
            'btci' : {
                'function' : self.get_btci,
                'kwargs_list' : [{'interval' :timedelta(minutes=1)}]
            },
            'candlesticks' :{
                'function' : self.get_candlestick,
                'kwargs_list' : [{'interval': str_to_datetime(x[1]), 'order_currency':x[0], 'chart_intervals':x[1]} for x in itertools.product(BITHUMB_TICKERS, BITHUMB_CANDLESTICK_INTERVALS)]
            }
        }
        self.max_calls_per_seconds = 30
        pass
        """

    '''
    def get_jobs(self) :

        return

    def get_scheulde(self) :

        return
    '''

    def get_tickers(self):
        requested_time = now()
        data = PublicApi.ticker('ALL')

        result = {'time': requested_time, 'data': data}
        return result

    def get_orderbooks(self):
        requested_time = now()
        data = PublicApi.orderbook('ALL', limit=30)

        result = {'time': requested_time, 'data': data}
        return result

    def get_transaction_history(self, order_currency):
        requested_time = now()
        data = PublicApi.transaction_history('BTC', limit=100)

        result = {'time': requested_time, 'data': data}
        return result

    def get_btci(self, order_currency):
        requested_time = now()
        data = PublicApi.btci()

        result = {'time': requested_time, 'data': data}
        return result

    def get_candlestick(self, order_currency, chart_intervals):
        requested_time = now()
        data = (PublicApi.candlestick(order_currency, chart_intervals),)

        result = {'time': requested_time, 'data': data}
        return result


def str_to_datetime(input_str):
    if 'h' in input_str:
        timestamp = timedelta(hours=int(input_str.replace('h', '')))
    elif 'm' in input_str:
        timestamp = timedelta(minutes=int(input_str.replace('m', '')))
    else:
        raise AssertionError('Cannot convert %s to timedelta' % input_str)
    return timestamp


BITHUMB_CANDLESTICK_INTERVALS = ['24h', '12h', '6h', '1h', '30m', '10m', '5m', '3m', '1m']


BITHUMB_TICKERS = [
    'BTC',
    'ETH',
    'DASH',
    'LTC',
    'ETC',
    'XRP',
    'BCH',
    'ZEC',
    'QTUM',
    'BTG',
    'EOS',
    'ICX',
    'TRX',
    'ELF',
    'OMG',
    'KNC',
    'GLM',
    'ZIL',
    'WAXP',
    'POWR',
    'LRC',
    'STEEM',
    'STRAX',
    'AE',
    'ZRX',
    'REP',
    'XEM',
    'SNT',
    'ADA',
    'CTXC',
    'BAT',
    'WTC',
    'THETA',
    'LOOM',
    'WAVES',
    'TRUE',
    'LINK',
    'RNT',
    'ENJ',
    'VET',
    'MTL',
    'IOST',
    'TMTG',
    'QKC',
    'BZNT',
    'HDAC',
    'NPXS',
    'WET',
    'AMO',
    'BSV',
    'DAC',
    'ORBS',
    'VALOR',
    'CON',
    'ANKR',
    'MIX',
    'LAMB',
    'CRO',
    'FX',
    'CHR',
    'MBL',
    'MXC',
    'OGO',
    'DVP',
    'FCT',
    'FNB',
    'TRV',
    'PCM',
    'DAD',
    'AOA',
    'XSR',
    'WOM',
    'SOC',
    'EM',
    'QBZ',
    'BOA',
    'FLETA',
    'SXP',
    'COS',
    'APIX',
    'EL',
    'BASIC',
    'HIVE',
    'XPR',
    'FIT',
    'EGG',
    'BORA',
    'ARPA',
    'APM',
    'ANW',
    'CENNZ',
    'EVZ',
    'MCI',
    'SRM',
    'QTCON',
    'UNI',
    'YFI',
    'UMA',
    'SAND',
    'CVT',
    'GOM2',
    'RINGX',
    'BEL',
    'DVC',
    'OBSR',
    'ORC',
    'POLA',
    'AWO',
    'ADP',
    'MIR',
    'WOZX',
    'ANV',
    'XNO',
    'BCD',
    'XLM',
    'PIVX',
    'GXC',
    'BTT',
    'HYC',
    'VSYS',
    'IPX',
    'WICC',
    'ONT',
    'LUNA',
    'AION',
    'META',
    'ONG',
    'ALGO',
    'JST',
    'XTZ',
    'MLK',
    'WEMIX',
    'DOT',
    'SUN',
    'ATOM',
    'BCHA',
    'TEMCO',
]

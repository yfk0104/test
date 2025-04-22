import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
import models.AbstractAccess as base

class WebAccess(base.AbstractAccess):
    FREQUENCY_DAY = 1

    def __init__(self, year) -> None:
        self._year = year

    def __del__(self) -> None:
        pass

    # 過去6年分のデータを取得
    def _get_price_data(self, ticker):
        # tickerを定義
        my_share = share.Share(ticker)
        symbol_data = None
        
        # データ取得
        try:
            symbol_data = my_share.get_historical(
                share.PERIOD_TYPE_YEAR, self._year,             # データ取得年数
                share.FREQUENCY_TYPE_DAY, self.FREQUENCY_DAY)   # 日足
        except YahooFinanceError as e:
            print(e.message)
            return None
        
        # DataFrameに変換
        df = pd.DataFrame(symbol_data)
        
        # timestampからdatetime, dateに変換
        df["datetime"] = pd.to_datetime(df.timestamp, unit="ms")
        df["date"] = df["datetime"].dt.date
        
        # date, open, high, low, close, volumeだけ抽出して返す
        #return df.set_index("date")[["close"]]
        return df.loc[:,['date','close']]

    def importData(self, selected_currency):
        currency = {
            'USD/JPY' : 'JPY=X',
            'EUR/JPY' : 'EURJPY=X',
            'EUR/USD' : 'EURUSD=X',
            'EUR/GBP' : 'EURGBP=X',
            'AUD/JPY' : 'AUDJPY=X',
            'AUD/USD' : 'AUDUSD=X',
            'AUD/NZD' : 'AUDNZD=X',
            'NZD/JPY' : 'NZDJPY=X',
            'NZD/USD' : 'NZDUSD=X',
            'CAD/JPY' : 'CADJPY=X',
            'USD/CAD' : 'CAD=X',
            'GBP/JPY' : 'GBPJPY=X',
            'GBP/USD' : 'GBPUSD=X',
            'TRY/JPY' : 'TRYJPY=X',
            'ZAR/JPY' : 'ZARJPY=X',
            'MXN/JPY' : 'MXNJPY=X',
        }

        df = self._get_price_data(currency[selected_currency])
        return df.values.tolist()


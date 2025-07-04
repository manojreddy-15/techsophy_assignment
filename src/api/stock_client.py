import yfinance as yf
from typing import List, Dict

class StockClient:
    def __init__(self, config):
        self.provider = config.get('provider', 'yfinance')

    def get_prices(self, symbols: List[str]) -> Dict[str, float]:
        data = {}
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            price = ticker.history(period='1d', interval='1m').tail(1)['Close']
            if not price.empty:
                data[symbol] = float(price.iloc[0])
            else:
                data[symbol] = None
        return data
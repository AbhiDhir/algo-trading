from enums import StockPeriod, StockInterval
from datetime import datetime
import yfinance as yf

class StockPriceFetcher:
    """
    Base Class for pulling data for a single Ticker using yfinance
    """
    def __init__():
        pass

    def fetch(ticker: str, period: StockPeriod=None, interval: StockInterval=None, start: datetime=None, end: datetime=datetime.now(), prepost: bool=False):
        if not (period and interval) and not start:
            raise Exception("Invalid parameters for StockPriceFetcher. Needs period and interval, or a start period")
        
        stock = yf.Ticker(ticker)
        
        if period and interval:
            return stock.history(period=period, interval=interval, prepost=prepost)
        
        return stock.history(start=start, end=end, prepost=prepost)
from enum import Enum
import functools

@functools.total_ordering
class BaseEnum(Enum):
    """Class to allow for comparison of time valued enums"""
    def __eq__(self, other):
        if isinstance(other, BaseEnum):
            return (
                self._member_names_.index(self.name) ==
                self._member_names_.index(other.name)
            )
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, BaseEnum):
            return (
                self._member_names_.index(self.name) >
                self._member_names_.index(other.name)
            )
        return NotImplemented

class StockPeriod(BaseEnum):
    """Enum for the time period for stock price collection"""
    DAY_1 = "1d"
    DAY_5 = "5d"
    MONTH_1 = "1mo"
    MONTH_3 = "3mo"
    MONTH_6 = "6mo"
    YEAR_1 = "1y"
    YEAR_2 = "2y"
    YEAR_5 = "5y"
    YEAR_10 = "10y"
    YTD = "ytd"
    MAX = "max"

class StockInterval(BaseEnum):
    """Enum for the interval for stock price collection"""
    MINUTE_1 = "1m"
    MINUTE_2 = "2m"
    MINUTE_5 = "5m"
    MINUTE_15 = "15m"
    MINUTE_30 = "30m"
    MINUTE_60 = "60m"
    MINUTE_90 = "90m"
    HOUR_1 = "1h"
    DAY_1 = "1d"
    DAY_5 = "5d"
    WEEK_1 = "1wk"
    MONTH_1 = "1mo"
    MONTH_3 = "3mo"
from pandas import Series as __Series
from scipy.stats import gmean
from functools import wraps
import pandas as pd

def percentile_for(percentile):
    def percentile_(series : __Series):
        return series.quantile(percentile / 100)
    percentile_.__name__ = 'percentile_{:2.0f}'.format(percentile)
    return percentile_


DEFAULT_STATS = ['min'] + [percentile_for(x) for x in range(10,91,10)] + ['max', 'mean', gmean]

def get_statistics(portfolio_values : pd.Series, statistics) -> pd.Series:
    statistics = list(map(lambda stat: _typecheck_series(stat) if callable(stat) else stat, statistics))
    statistics = portfolio_values.agg(statistics)
    statistics.index.name = "Statistic"
    return statistics


def _typecheck_series(func):
    @wraps(func)
    def wrapper(series):
        if isinstance(series, pd.Series):
            return func(series)
        else:
            raise TypeError
    return wrapper
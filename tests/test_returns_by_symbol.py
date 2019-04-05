"""
pytests for returns_by_symbol module
"""

import pytest
from pandas.util.testing import assert_frame_equal
from pandas.util.testing import assert_series_equal
import pandas as pd

import portfoliofinder as pf

from testdata_constants import *



def test_init():
    df = pd.DataFrame({'a':[1],'b':[2]})
    returns_by_symbol = pf.ReturnsBySymbol(df)

    actual_df = returns_by_symbol.to_dataframe()

    assert_frame_equal(df, actual_df)

def test_from_csv():
    """tests fetch_all_returns_from_csv"""
    actual_returns = pf.ReturnsBySymbol.from_csv("tests/test_data.csv")

    assert_frame_equal(actual_returns.to_dataframe(), EXPECTED_ALL_RETURNS)


def test_get_specific_returns():
    """tests get_specific_returns"""
    all_returns = pf.ReturnsBySymbol(EXPECTED_ALL_RETURNS)

    actual_specific_returns = all_returns.filter_by_symbols(SPECIFIC_FUNDS)

    assert_frame_equal(actual_specific_returns.to_dataframe(), EXPECTED_SPECIFIC_RETURNS)

def test_adjust_for_inflation():
    """tests get_inflation_adjusted_returns"""
    actual_inflation_adjusted_returns = DEFAULT_SPECIFIC_RETURNS_BY_SYMBOL.adjust_for_inflation(EXPECTED_INFLATION_RATES)

    assert_frame_equal(actual_inflation_adjusted_returns.to_dataframe(), EXPECTED_INFLATION_ADJUSTED_SPECIFIC_RETURNS)

from functools import reduce
from typing import Callable

import pandas as pd


class DataSchema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    MONTH = "month"
    YEAR = "year"


Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


def create_year_column(df: pd.DataFrame) -> pd.DataFrame:
    df_temp = df.copy()
    df_temp[DataSchema.YEAR] = df_temp[DataSchema.DATE].dt.year.astype(str)
    return df_temp


def create_month_column(df: pd.DataFrame) -> pd.DataFrame:
    df_temp = df.copy()
    df_temp[DataSchema.MONTH] = df_temp[DataSchema.DATE].dt.month.astype(str)
    return df_temp


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={DataSchema.AMOUNT: float, DataSchema.CATEGORY: str},
        parse_dates=[DataSchema.DATE],
    )
    preprocessor = compose(create_year_column, create_month_column)
    return preprocessor(data)

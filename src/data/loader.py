import datetime as dt
from functools import partial, reduce
from typing import Callable

import babel.dates
import i18n
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


def translate_date(df: pd.DataFrame, locale: str) -> pd.DataFrame:
    def date_repr(date: dt.date) -> str:
        return babel.dates.format_date(date, format="MMMM", locale=locale)

    df[DataSchema.MONTH] = df[DataSchema.DATE].apply(date_repr)
    return df


def translate_category(df: pd.DataFrame) -> pd.DataFrame:
    def translate(category: str) -> str:
        return i18n.t(f"category.{category}")

    df[DataSchema.CATEGORY] = df[DataSchema.CATEGORY].apply(translate)
    return df


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def load_transaction_data(path: str, locale: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={DataSchema.AMOUNT: float, DataSchema.CATEGORY: str},
        parse_dates=[DataSchema.DATE],
    )
    preprocessor = compose(
        create_year_column,
        create_month_column,
        partial(translate_date, locale=locale),
        translate_category,
    )
    return preprocessor(data)

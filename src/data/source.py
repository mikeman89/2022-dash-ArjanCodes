from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from .loader import DataSchema


@dataclass
class DataSource:
    _data: pd.DataFrame

    def filter(
        self,
        years: Optional[list[str]],
        months: Optional[list[str]],
        categories: Optional[list[str]],
    ) -> DataSource:
        if years is None:
            years = self.unique_years
        if months is None:
            months = self.unique_months
        if categories is None:
            categories = self.unique_categories
        filtered_data = self._data.loc[
            self._data[DataSchema.YEAR].isin(years)
            & self._data[DataSchema.MONTH].isin(months)
            & self._data[DataSchema.CATEGORY].isin(categories)
        ]
        return DataSource(filtered_data)

    @property
    def all_years(self) -> list[str]:
        return self._data[DataSchema.YEAR].tolist()

    @property
    def unique_years(self) -> list[str]:
        return sorted(set(self.all_years), key=int)

    @property
    def all_months(self) -> list[str]:
        return self._data[DataSchema.MONTH].tolist()

    @property
    def unique_months(self) -> list[str]:
        return sorted(set(self.all_months), key=int)

    @property
    def all_categories(self) -> list[str]:
        return self._data[DataSchema.CATEGORY].tolist()

    @property
    def unique_categories(self) -> list[str]:
        return sorted(set(self.all_categories), key=int)

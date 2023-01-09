from __future__ import annotations

from typing import Optional, Protocol

import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.source import DataSource

from . import ids


class MonthsDataSource(Protocol):
    def filter(
        self,
        years: Optional[list[str]] = None,
        months: Optional[list[str]] = None,
        categories: Optional[list[str]] = None,
    ) -> MonthsDataSource:
        ...

    @property
    def unique_months(self) -> list[str]:
        ...


def render(app: Dash, source: MonthsDataSource) -> html.Div:
    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
        ],
    )
    def update_months(years: list[str], _: int) -> list[str]:
        return source.filter(years=years).unique_months

    return html.Div(
        children=[
            html.H6(i18n.t("general.month")),
            dcc.Dropdown(
                multi=True,
                options=[
                    {"label": month, "value": month} for month in source.unique_months
                ],
                id=ids.MONTH_DROPDOWN,
                value=source.unique_months,
            ),
            html.Button(
                className="dropdown-button",
                children=[i18n.t("general.select_all")],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            ),
        ]
    )

import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_categories: list[str] = data[DataSchema.CATEGORY].tolist()
    unique_categories = sorted(set(all_categories))

    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks"),
        ],
    )
    def update_months(years: list[str], months: list[str], _: int) -> list[str]:
        filtered_data = data.loc[
            data[DataSchema.YEAR].isin(years) & data[DataSchema.MONTH].isin(months)
        ]
        return sorted(set(filtered_data[DataSchema.CATEGORY].tolist()))

    return html.Div(
        children=[
            html.H6("Categories"),
            dcc.Dropdown(
                multi=True,
                options=[
                    {"label": category, "value": category}
                    for category in unique_categories
                ],
                id=ids.CATEGORY_DROPDOWN,
                value=unique_categories,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                n_clicks=0,
            ),
        ]
    )

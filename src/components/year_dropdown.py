import i18n
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_years: list[str] = data[DataSchema.YEAR].tolist()
    unique_years = sorted(set(all_years))

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks")],
    )
    def select_all_years(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            html.H6(i18n.t("general.year")),
            dcc.Dropdown(
                multi=True,
                options=[{"label": year, "value": year} for year in unique_years],
                id=ids.YEAR_DROPDOWN,
                value=unique_years,
            ),
            html.Button(
                className="dropdown-button",
                children=[i18n.t("general.select_all")],
                id=ids.SELECT_ALL_YEARS_BUTTON,
                n_clicks=0,
            ),
        ]
    )

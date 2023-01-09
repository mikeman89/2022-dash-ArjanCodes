import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.source import DataSource

from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks")],
    )
    def select_all_years(_: int) -> list[str]:
        return source.unique_years

    return html.Div(
        children=[
            html.H6(i18n.t("general.year")),
            dcc.Dropdown(
                multi=True,
                options=[
                    {"label": year, "value": year} for year in source.unique_years
                ],
                id=ids.YEAR_DROPDOWN,
                value=source.unique_years,
            ),
            html.Button(
                className="dropdown-button",
                children=[i18n.t("general.select_all")],
                id=ids.SELECT_ALL_YEARS_BUTTON,
                n_clicks=0,
            ),
        ]
    )

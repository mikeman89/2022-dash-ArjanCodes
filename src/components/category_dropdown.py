import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.source import DataSource

from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    source.unique_categories

    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks"),
        ],
    )
    def update_months(years: list[str], months: list[str], _: int) -> list[str]:
        return source.filter(years=years, months=months).unique_categories

    return html.Div(
        children=[
            html.H6(i18n.t("general.category")),
            dcc.Dropdown(
                multi=True,
                options=[
                    {"label": category, "value": category}
                    for category in source.unique_categories
                ],
                id=ids.CATEGORY_DROPDOWN,
                value=source.unique_categories,
            ),
            html.Button(
                className="dropdown-button",
                children=[i18n.t("general.select_all")],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                n_clicks=0,
            ),
        ]
    )

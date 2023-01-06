from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash) -> html.Div:
    all_nations = ["South Korea", "China", "Canada"]

    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        [Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks")],
    )
    def select_all_nations(_: int) -> list[str]:
        return all_nations

    return html.Div(
        children=[
            html.H6("Nations"),
            dcc.Dropdown(
                multi=True,
                options=[{"label": nation, "value": nation} for nation in all_nations],
                id=ids.NATION_DROPDOWN,
                value=all_nations,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_NATIONS_BUTTON,
            ),
        ]
    )

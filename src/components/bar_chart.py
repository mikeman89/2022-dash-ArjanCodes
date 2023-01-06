import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids

MEDAL_DATA: pd.DataFrame = px.data.medals_long()


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"), [Input(ids.NATION_DROPDOWN, "value")]
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        filtered_data = MEDAL_DATA.loc[MEDAL_DATA["nation"].isin(nations)]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(
            children=[
                dcc.Graph(figure=fig, id=ids.BAR_CHART),
                html.Div(
                    "list of nations selected: {}".format(nations), id="nation-list"
                ),
            ]
        )

    return html.Div(id=ids.BAR_CHART)

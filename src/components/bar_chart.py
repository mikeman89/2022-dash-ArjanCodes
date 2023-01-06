import plotly.express as px
from dash import Dash, dcc, html

from . import ids

MEDAL_DATA = px.data.metals_long()


def render(app: Dash) -> html.Div:
    fig = px.bar(MEDAL_DATA, x="medal", y="count", color="nation", text="nation")
    return html.Div(dcc.Graph(figure=fig, id=ids.BAR_CHART))

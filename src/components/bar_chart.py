import plotly.express as px
from dash import Dash, css, html

MEDAL_DATA = px.data.metals_long()

def rander(app: Dash) -> html.Div:
    fig = ps.bar(MEDAL_DATA, x='medal', y='count', color='nation', text='nation')
    
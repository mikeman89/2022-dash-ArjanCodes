import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.PIE_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_DROPDOWN, "value"),
        ],
    )
    def update_pie_chart(
        years: list[str], months: list[str], categories: list[str]
    ) -> html.Div:
        filtered_data = data.loc[
            data[DataSchema.YEAR].isin(years)
            & data[DataSchema.MONTH].isin(months)
            & data[DataSchema.CATEGORY].isin(categories)
        ]
        if filtered_data.empty:
            return html.Div("No data available")

        fig = px.pie(
            data_frame=filtered_data,
            names=filtered_data[DataSchema.CATEGORY].to_list(),
            values=filtered_data[DataSchema.AMOUNT].to_list(),
            hole=0.5,
        )
        fig.update_layout(margin={"t": 40, "b": 0, "l": 0, "r": 0})
        fig.update_traces(hovertemplate="%{label}<br>$%{value:.2f}<extra></extra>")

        return html.Div(dcc.Graph(figure=fig), id=ids.PIE_CHART)

    return html.Div(id=ids.PIE_CHART)

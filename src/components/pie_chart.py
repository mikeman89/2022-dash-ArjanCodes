from calendar import month

import i18n
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.source import DataSource

from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
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
        filtered_data = source.filter(years, months, categories)
        if filtered_data.is_empty:
            return html.Div(i18n.t("general.no_data"))

        fig = px.pie(
            data_frame=filtered_data.data,
            names=filtered_data.all_categories,
            values=filtered_data.all_amounts,
            hole=0.5,
        )
        fig.update_layout(margin={"t": 40, "b": 0, "l": 0, "r": 0})
        fig.update_traces(hovertemplate="%{label}<br>$%{value:.2f}<extra></extra>")

        return html.Div(dcc.Graph(figure=fig), id=ids.PIE_CHART)

    return html.Div(id=ids.PIE_CHART)

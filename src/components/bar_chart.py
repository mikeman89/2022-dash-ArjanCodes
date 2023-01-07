import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_DROPDOWN, "value"),
        ],
    )
    def update_bar_chart(
        years: list[str], months: list[str], categories: list[str]
    ) -> html.Div:
        filtered_data = data.loc[
            data[DataSchema.YEAR].isin(years)
            & data[DataSchema.MONTH].isin(months)
            & data[DataSchema.CATEGORY].isin(categories)
        ]
        if filtered_data.empty:
            return html.Div("No data available")

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.AMOUNT,
                index=DataSchema.CATEGORY,
                aggfunc="sum",
                fill_value=0,
            )
            return pt.reset_index().sort_values(by=DataSchema.AMOUNT, ascending=False)

        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY,
        )
        fig.update_traces(hovertemplate="%{x}<br>$%{y:.2f}<extra></extra>")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)

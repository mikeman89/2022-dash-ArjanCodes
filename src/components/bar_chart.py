import i18n
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.data.loader import DataSchema
from src.data.source import DataSource

from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
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
        filtered_data = source.filter(years, months, categories)
        if filtered_data.is_empty:
            return html.Div(i18n.t("general.no_data"))

        fig = px.bar(
            filtered_data.create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY,
            labels={
                DataSchema.CATEGORY: i18n.t("general.category"),
                DataSchema.AMOUNT: i18n.t("general.amount"),
            },
        )
        fig.update_traces(hovertemplate="%{x}<br>$%{y:.2f}<extra></extra>")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)

from cProfile import label
from unicodedata import name
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
from preprocessing import get_assets

app = Dash(__name__, suppress_callback_exceptions=True)

assets = get_assets()

assets_sale_count = assets['last_sale_payment_token_symbol'].value_counts()
assets_sale_count_df = pd.DataFrame({'token': assets_sale_count.index, 'count': assets_sale_count.values})
fig = px.pie(assets_sale_count_df, values="count", names="token")


app.layout = html.Div(children=[
	html.H1("Fee Basis Points & Total Transactions vs. Total Price"),
	html.Div(
        dcc.Graph(id="pie_plt", figure=fig)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
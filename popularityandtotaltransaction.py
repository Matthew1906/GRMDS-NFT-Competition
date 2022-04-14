import pandas as pd
import numpy as np

assets = pd.read_csv('./cleaned-datasets/cleaned_assets.csv')
collections = pd.read_csv('./cleaned-datasets/cleaned_collections.csv')
events = pd.read_csv('./cleaned-datasets/cleaned_events.csv')

assets['asset_contract_created_date'] = pd.to_datetime(assets['asset_contract_created_date'], format='%Y-%m-%dT%H:%M:%S')

## Adding year created in assets dataframe
assets['created_year'] = assets['asset_contract_created_date'].dt.year

from dash import Dash, dcc, html, dash_table
import plotly.graph_objs as go
from plotly.subplots import make_subplots

app = Dash(__name__)

fig = make_subplots(rows=3, cols=1, subplot_titles=("Scatter plot of asset favorites and last sale total price", "Scatter plot of asset favorites and num sales", "Scatter plot of num sales and last sale total price"))

fig.add_trace(go.Scatter(x=assets['asset_favorites'], y=assets['last_sale_total_price'], mode='markers'), row=1, col=1)
fig.add_trace(go.Scatter(x=assets['asset_favorites'], y=assets['num_sales'], mode='markers'), row=2, col=1)
fig.add_trace(go.Scatter(x=assets['num_sales'], y=assets['last_sale_total_price'], mode='markers'), row=3, col=1)

fig.update_xaxes(title_text="Asset Favorites", row=1, col=1)
fig.update_xaxes(title_text="Asset Favorites", row=2, col=1)
fig.update_xaxes(title_text="Num Sales", row=3, col=1)

fig.update_yaxes(title_text="Last Sale Total Price", row=1, col=1)
fig.update_yaxes(title_text="Num Sales", row=2, col=1)
fig.update_yaxes(title_text="Last Sale Total Price", row=3, col=1)

fig.update_layout(height=700, showlegend=False)

app.layout = html.Div(children=[
    html.H1('How popularity & total transactions affect an NFT price'),
    dcc.Graph(
        figure = fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
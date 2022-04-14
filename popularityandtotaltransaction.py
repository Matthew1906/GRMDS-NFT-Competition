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
import plotly.express as px
from preprocessing import get_assets

assets = get_assets()
assets_sold = assets[assets['last_sale_created_date'].notna()]

app = Dash(__name__)

this_figure = make_subplots(rows=3, cols=1, subplot_titles=("Fee Basis Points vs Total Price", "Scatter plot of asset favorites and last sale total price", "Scatter plot of num sales and last sale total price"))

figure1 = px.scatter(assets_sold, x='last_sale_total_price', 
                y='asset_contract_dev_seller_fee_basis_points',
                color_discrete_sequence=["red"],
                trendline="ols",
                trendline_color_override="red")

figure2 = px.scatter(assets, x='last_sale_total_price',
                y='asset_favorites',
                color_discrete_sequence=["blue"],
                trendline='ols',
                trendline_color_override="blue")

figure4 = px.scatter(assets, x='last_sale_total_price',
                y='num_sales', 
                color_discrete_sequence=["orange"],
                trendline='ols',
                trendline_color_override="orange")

figure1_traces = []
figure2_traces = []
figure4_traces = []

for trace in range(len(figure1["data"])):
    figure1_traces.append(figure1["data"][trace])
    
for trace in range(len(figure2["data"])):
    figure2_traces.append(figure2["data"][trace])

for trace in range(len(figure4["data"])):
    figure4_traces.append(figure4["data"][trace])

for traces in figure1_traces:
    this_figure.append_trace(traces, row=1, col=1)

for traces in figure2_traces:
    this_figure.append_trace(traces, row=2, col=1)
    
for traces in figure4_traces:
    this_figure.append_trace(traces, row=3, col=1)

this_figure.update_layout(height=1000, showlegend=False)

this_figure.update_xaxes(title_text='Last Sale Total Price', row=1, col=1)
this_figure.update_xaxes(title_text='Last Sale Total Price', row=2, col=1)
this_figure.update_xaxes(title_text='Last Sale Total Price', row=3, col=1)

this_figure.update_yaxes(title_text='Asset Contract Dev Seller Basis Points', row=1, col=1)
this_figure.update_yaxes(title_text='Asset Favorites', row=2, col=1)
this_figure.update_yaxes(title_text='Num Sales', row=3, col=1)

app.layout = html.Div(children=[
    html.H1('How popularity & total transactions affect an NFT price'),
    dcc.Graph(
        figure = this_figure
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
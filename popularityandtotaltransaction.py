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

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('How popularity & total transactions affect an NFT price'),
    html.Div(children=[
        html.Div(
            dcc.Graph(
                id='scatter1',
                figure = {
                    'data': [
                        go.Scatter(
                            x = assets['asset_favorites'],
                            y = assets['last_sale_total_price'],
                            mode = 'markers'
                        )
                    ],
                    'layout': go.Layout(
                        title = 'Scatter plot of asset favorites and last sale total price',
                        xaxis = {'title': 'Asset Favorites'},
                        yaxis = {'title': 'Last Sale Total Price'}
                    )
                }
            )
        )
    ]),
    html.Div(children=[
        html.Div(
            dcc.Graph(
                id='scatter2',
                figure = {
                    'data': [
                        go.Scatter(
                            x = assets['asset_favorites'],
                            y = assets['num_sales'],
                            mode = 'markers'
                        )
                    ],
                    'layout': go.Layout(
                        title = 'Scatter plot of asset favorites and num sales',
                        xaxis = {'title': 'Asset Favorites'},
                        yaxis = {'title': 'Num Sales'}
                    )
                }
            )
        )
    ]),
    html.Div(children=[
        html.Div(
            dcc.Graph(
                id='scatter3',
                figure = {
                    'data': [
                        go.Scatter(
                            x = assets['num_sales'],
                            y = assets['last_sale_total_price'],
                            mode = 'markers'
                        )
                    ],
                    'layout': go.Layout(
                        title = 'Scatter plot of num sales and last sale total price',
                        xaxis = {'title': 'Num Sales'},
                        yaxis = {'title': 'Last Sale Total Price'}
                    )
                }
            )
        )
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
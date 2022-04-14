import dash_bootstrap_components as dbc
from dash import dcc, html

def get_layout():
    return dbc.Container(
        children=[
            html.H1('NFT Asset Category Comparison'),
            dcc.Dropdown(
                options = ['Last Sale Total Price', 'Asset Favorites', 'Num Sales'],
                value = 'Last Sale Total Price',
                id='asset-category-compare-choice'
            ),
            dcc.Graph(id='asset-category-compare-graph')
        ]
    )
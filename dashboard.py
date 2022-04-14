# PREPARING DATASETS
from preprocessing import *
import pandas as pd
import numpy as np

## Loading Datasets + Data prep
assets = get_assets()
events = get_events()
collections = get_collections()

## Generate visualizations (plots, data tables)



# DASHBOARD
from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(children=[
    ### Interactive Dashboard
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Row(children=[
                html.H4("NFT Transactions")
            ], className="bg-secondary"),
            dbc.Row(children=[
                html.H4("NFT Asset Category Comparison")
            ], className="bg-secondary")
        ], className="col-sm-12 col-md-12 col-lg-5 bg-primary p-2"),
        dbc.Col(children=[
            html.H4("Collections Comparison")
        ], className="col-sm-12 col-md-12 col-lg-7 bg-primary p-2")
    ], className="bg-success p-2"),
    ### Static Dashboard
    dbc.Row(children=[
        dbc.Col(children=[
            html.H4("Fee Basis Points, Popularity, Total Transactions vs. NFT Price")
        ], className="col-sm-12 col-md-12 col-lg-7 bg-secondary"),
        dbc.Col(children=[
            dbc.Row(children=[
                html.H4("Best Listing Duration")
            ], className="bg-secondary"),
            dbc.Row(children=[
                html.H4("Tokens Statistics for Transaction")
            ], className="bg-secondary")
        ], className="col-sm-12 col-md-12 col-lg-5")
    ], className="bg-primary p-2")
])

if __name__ == "__main__":
    app.run_server(debug=True)
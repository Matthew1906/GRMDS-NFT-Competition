# Standard Modules
import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table
# Preprocessing
from .preprocessing import *
# Controllers
from .controllers import \
    asset_category_comparison as acc_controller, \
    collection_comparison as cc_controller, \
    transactions as t_controller
# Views
from .views import \
    asset_category_comparison as acc_view, \
    best_listing_time as blt_view, \
    collection_comparison as cc_view, \
    fee_popularity as fp_view,\
    statistics as s_view, \
    transactions as t_view

# Get 
assets = get_assets()
collections = get_collections()
events = get_events()
listing = get_listings()

def create_app():
    '''Build Dashboard'''
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
    
    app.layout = dbc.Container(children=[
        # dbc.Row(children=[
        #     dbc.Col(children=[
        #         dbc.Row(children=[
        #             html.H4("NFT Transactions")
        #         ], className="bg-secondary"),
        #         dbc.Row(children=[
        #             html.H4("NFT Asset Category Comparison")
        #         ], className="bg-secondary")
        #     ], className="col-sm-12 col-md-12 col-lg-5 bg-primary p-2"),
        #     dbc.Col(children=[
        #         html.H4("Collections Comparison")
        #     ], className="col-sm-12 col-md-12 col-lg-7 bg-primary p-2")
        # ], className="bg-success p-2"),
        # ### Static Dashboard
        # dbc.Row(children=[
        #     dbc.Col(children=[
        #         html.H4("Fee Basis Points, Popularity, Total Transactions vs. NFT Price")
        #     ], className="col-sm-12 col-md-12 col-lg-7 bg-secondary"),
        #     dbc.Col(children=[
        #         dbc.Row(children=[
        #             html.H4("Best Listing Duration")
        #         ], className="bg-secondary"),
        #         dbc.Row(children=[
        #             html.H4("Tokens Statistics for Transaction")
        #         ], className="bg-secondary")
        #     ], className="col-sm-12 col-md-12 col-lg-5")
        # ], className="bg-primary p-2")
        acc_view.get_layout(),
        blt_view.get_layout(best_listing=listing),
        cc_view.get_layout(),
        fp_view.get_layout(assets=assets),
        s_view.get_layout(assets=assets),
        t_view.get_layout()
    ])

    acc_controller.get_callbacks(app=app, assets=assets)
    cc_controller.get_callbacks(app=app, collections=collections)
    t_controller.get_callbacks(app=app, assets=assets)

    return app
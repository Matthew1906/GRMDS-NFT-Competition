# Standard Modules
import pandas as pd
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

ext_script = ["https://cdn.tailwindcss.com"]
ext_stylesheet = ["https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"]


def create_app():
    '''Build Dashboard'''
    app = Dash(__name__, external_scripts=ext_script, external_stylesheets=ext_stylesheet,suppress_callback_exceptions=True)

    app.scripts.config.serve_locally = True
    
    app.layout = html.Div(children=[
        html.H1(
            children=['NFT Transactions Dashboard'],
            className="text-center text-4xl pt-10 pb-2 font-semibold"
        ),
        html.P(
            children=['By Team Kebab'],
            className="text-center pb-6"
        ),
        html.Div(children=[  
            t_view.get_layout(),
            acc_view.get_layout(),
            blt_view.get_layout(best_listing=listing),
            s_view.get_layout(assets=assets),
            cc_view.get_layout(),
            fp_view.get_layout(assets=assets),
        ], className="grid grid-cols-12 px-10 pt-2 pb-8 gap-6"),
    ], className="bg-slate-200"
    )

    acc_controller.get_callbacks(app=app, assets=assets)
    cc_controller.get_callbacks(app=app, collections=collections)
    t_controller.get_callbacks(app=app, assets=assets)

    return app
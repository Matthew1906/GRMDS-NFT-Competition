from preprocessing import *
import pandas as pd
import numpy as np

assets = get_assets()
events = get_events()
collections = get_collections()

top10nft = assets.sort_values('num_sales', ascending=False)[['collection_slug','token_id','name','asset_category','created_year','num_sales']].head(10)

from dash import Dash, dcc, html, dash_table

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Top 10 NFT Transactions'),
    html.Div(
        children=dash_table.DataTable(top10nft.to_dict('records'), [{"name": i, "id": i} for i in top10nft.columns]), 
        style={
            'width': '720px'
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
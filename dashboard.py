import pandas as pd
import numpy as np

assets = pd.read_csv('./cleaned-datasets/cleaned_assets.csv')
collections = pd.read_csv('./cleaned-datasets/cleaned_collections.csv')
events = pd.read_csv('./cleaned-datasets/cleaned_events.csv')

assets['asset_contract_created_date'] = pd.to_datetime(assets['asset_contract_created_date'], format='%Y-%m-%dT%H:%M:%S')

## Adding year created in assets dataframe
assets['created_year'] = assets['asset_contract_created_date'].dt.year

top10nft = assets.sort_values('num_sales', ascending=False)[['collection_slug','token_id','name','asset_category','created_year','num_sales']].head(10)

from dash import Dash, dcc, html, dash_table

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Top 10 NFT Transactions'),
    html.Div(child=dash_table.DataTable(top10nft.to_dict('records'), [{"name": i, "id": i} for i in top10nft.columns]), 
        style={
            'width': '720px'
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
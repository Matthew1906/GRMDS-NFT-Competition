import pandas as pd
import numpy as np

assets = pd.read_csv('./cleaned-datasets/cleaned_assets.csv')
collections = pd.read_csv('./cleaned-datasets/cleaned_collections.csv')
events = pd.read_csv('./cleaned-datasets/cleaned_events.csv')

assets['asset_contract_created_date'] = pd.to_datetime(assets['asset_contract_created_date'], format='%Y-%m-%dT%H:%M:%S')

## Adding year created in assets dataframe
assets['created_year'] = assets['asset_contract_created_date'].dt.year

aggregate = {
    'stats_total_volume': 'mean',
    'stats_market_cap': 'mean',
    'stats_total_sales': 'mean',
    'stats_num_owners': 'sum',
    'stats_average_price': 'sum'
}
collections_by_slug = collections.groupby('slug')[['stats_total_volume', 'stats_market_cap', 'stats_total_sales', 'stats_num_owners', 'stats_average_price']].agg(aggregate).sort_values('stats_total_sales', ascending=False)
collections_by_slug.reset_index(inplace=True)

from dash import Dash, dcc, html, dash_table

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Collection Comparison'),
    html.Div(
        children=dash_table.DataTable(collections_by_slug.head(10).to_dict('records'), [{"name": i, "id": i} for i in collections_by_slug.columns]), 
        style={
            'width': '720px'
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
import plotly.express as px
from dash import Dash, dcc, html, dash_table, Input, Output
from preprocessing import get_assets

assets = get_assets()

aggregate = {
    'last_sale_total_price': 'mean',
    'asset_favorites': 'sum',
    'num_sales': 'sum'
}

category_comparison = assets.groupby('asset_category')[['last_sale_total_price', 'asset_favorites', 'num_sales']]\
    .agg(aggregate).sort_values('num_sales', ascending=False)

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    children=[
        html.H1('NFT Asset Category Comparison'),
        dcc.Dropdown(
            options = ['last_sale_total_price', 'asset_favorites', 'num_sales'],
            value = ['last_sale_total_price'],
            id='asset-category-compare-choice'
        ),
        dcc.Graph(id='asset-category-compare-graph')
    ]
)

@app.callback(
    Output(component_id='asset-category-compare-graph', component_property='figure'),
    Input(component_id='asset-category-compare-choice', component_property='value'),
)
def update_graph(choice):
    return px.bar(data_frame = category_comparison.reset_index(), x='asset_category', y=choice)

if __name__ == "__main__":
    app.run_server(debug=True)
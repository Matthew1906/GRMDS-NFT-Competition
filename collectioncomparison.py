import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, Input, Output

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

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    children=[
        html.H1('Collection Comparison'),
        dcc.Dropdown(
            options = ['stats_total_volume', 'stats_market_cap', 'stats_total_sales', 'stats_num_owners', 'stats_average_price'],
            value = ['stats_total_volume'],
            id='collection-comparison-choice'
        ),
        dcc.Graph(id='collection-comparison-graph')
    ]
)

@app.callback(
    Output(component_id='collection-comparison-graph', component_property='figure'),
    Input(component_id='collection-comparison-choice', component_property='value'),
)
def update_graph(choice):
    fig = px.bar(data_frame = collections_by_slug.reset_index().head(100), x=choice, y='slug', color='slug')
    fig.update_layout(height=2000, yaxis={'categoryorder':'total ascending'}, showlegend=False)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
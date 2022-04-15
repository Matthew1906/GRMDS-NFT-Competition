import plotly.express as px
from dash import Input, Output

aggregate = {
    'Last Sale Total Price':'mean',
    'Asset Favorites':'sum',
    'Num Sales':'sum'
}

def get_callbacks(app, assets):
    '''Get Callbacks related to Asset Category Comparison'''
    # Generate dataset
    category_comparison = assets.groupby('Asset Category')[['Last Sale Total Price', 'Asset Favorites', 'Num Sales']]\
        .agg(aggregate).sort_values('Num Sales', ascending=False).reset_index()
    category_comparison['Asset Category'] = category_comparison['Asset Category'].str.replace('&', ' & ')
    category_comparison['Asset Category'] = category_comparison['Asset Category'].str.replace('-', ' ')
    category_comparison['Asset Category'] = category_comparison['Asset Category'].str.title()
    category_comparison['Last Sale Total Price'] = category_comparison['Last Sale Total Price']//10e15
    # Update Graph
    @app.callback(
        Output(component_id = 'asset-category-compare-graph', component_property = 'figure'),
        Input(component_id = 'asset-category-compare-choice', component_property = 'value'),
    )
    def update_graph(choice):
        fig = px.bar(
            data_frame = category_comparison.sort_values(choice, ascending = False), 
            x = 'Asset Category', 
            y = choice,
            color = 'Asset Category'
        )
        fig.update_layout(
            yaxis_title = f"Sum of {choice}" if choice != 'Last Sale Total Price' else f"Mean of {choice} (Quadrillion)", 
            showlegend = False
        )
        return fig
        
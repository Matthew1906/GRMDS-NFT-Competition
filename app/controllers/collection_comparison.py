import plotly.express as px
from dash import Input, Output

aggregate = {
    'Stats Total Volume': 'mean',
    'Stats Market Cap': 'mean',
    'Stats Total Sales': 'mean',
    'Stats Num Owners': 'sum',
    'Stats Average Price': 'sum'
}

def get_callbacks(app, collections):
    collections_by_slug = collections.groupby('Slug')[['Stats Total Volume', 'Stats Market Cap', 'Stats Total Sales', 'Stats Num Owners', 'Stats Average Price']].agg(aggregate).sort_values('Stats Total Sales', ascending=False)
    
    @app.callback(
        Output(component_id='collection-comparison-graph', component_property='figure'),
        Input(component_id='collection-comparison-choice', component_property='value'), 
    )
    def update_graph(choice):
        fig = px.bar(data_frame = collections_by_slug.reset_index().head(100), x=choice, y='Slug', color='Slug')
        fig.update_layout(height=2000, yaxis={'categoryorder':'total ascending'}, showlegend=False)
        return fig
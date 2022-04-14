from dash import dcc, html

def get_layout():
    return html.Div(
        children=[
            html.H1('Collection Comparison'),
            dcc.Dropdown(
                options = ['Stats Total Volume', 'Stats Market Cap', 'Stats Total Sales', 'Stats Num Owners', 'Stats Average Price'],
                value = ['Stats Total Volume'],
                id='collection-comparison-choice'
            ),
            dcc.Graph(id='collection-comparison-graph')
        ]
    )
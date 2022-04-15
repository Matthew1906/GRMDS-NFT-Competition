from dash import dcc, html

def get_layout():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H1('Collection Comparison', className="font-semibold text-xl"),
                    dcc.Dropdown(
                        options = ['Stats Total Volume', 'Stats Market Cap', 'Stats Total Sales', 'Stats Num Owners', 'Stats Average Price'],
                        value = ['Stats Total Volume'],
                        id='collection-comparison-choice'
                    ),
                ],
                className="flex flex-col gap-6"
            ),
            html.Div(
                dcc.Graph(id='collection-comparison-graph'),
                className="h-[62rem] overflow-y-scroll"
            )
        ],
        className="col-span-8 row-span-2 bg-white p-8 rounded-md shadow-md flex flex-col justify-between gap-4"
    )
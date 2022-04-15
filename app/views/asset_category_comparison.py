from dash import dcc, html

def get_layout():
    ''' Get Layout for Asset Category Comparison'''
    return html.Div(
        children = [
            html.Div(
                children = [
                    html.H1(
                        children = ['NFT Asset Category Comparison'], 
                        className = "font-semibold text-xl"
                    ),
                    dcc.Dropdown(
                        id = 'asset-category-compare-choice',
                        options = ['Last Sale Total Price', 'Asset Favorites', 'Num Sales'],
                        value = 'Last Sale Total Price'
                    )
                ],
                className = "flex flex-col gap-6"
            ),
            dcc.Graph(id = 'asset-category-compare-graph')
        ],
        className = "bg-white p-8 rounded-md shadow-md flex flex-col gap-2 col-span-5"
    )
    
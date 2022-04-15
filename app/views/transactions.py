from dash import html, dcc

def get_layout():
    '''Get Layout for Transactions'''
    return html.Div(
        children = [
            html.H1(
                id = 'transaction-heading',
                children = ['NFT Transactions Analysis'], 
                className = "font-semibold text-xl"
            ),
            html.Div(
                id = 'transaction',
                children = [
                    html.Div(
                        children = [
                            dcc.Dropdown(
                                id = 'transaction-choose-category',
                                options = [
                                    'Top 10 NFT', 
                                    'Asset Category',
                                    'Collection Slug', 
                                    'Created Year'
                                ],
                                value = 'Top 10 NFT',
                                style = {'width': '100%'}
                            ),
                            html.Div(
                                id = 'transaction-choose-options',
                                children = [
                                    dcc.Dropdown(
                                        id = 'transaction-choose-option',
                                        options = ['None'],
                                        value = 'None'
                                    )
                                ],
                            ),
                        ],
                        className = "flex items-center"
                    ),
                    html.Div(
                        id = 'transaction-choose-content',
                        children = [],
                    )
                ],
                className = "flex flex-col gap-8"
            )
        ],
        className = "bg-white p-8 rounded-md shadow-md col-span-7 flex flex-col gap-6"
    )

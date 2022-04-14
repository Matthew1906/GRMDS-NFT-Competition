from dash import html, dcc

def get_layout():
    return html.Div(
        children=[
            html.H1('NFT Transactions Analysis', id='transaction-heading'),
            html.Div(
                id='transaction',
                children=[
                    html.Div(
                        style = {'display':'flex', 'justifyContent':'center', 'alignItems':'center'},
                        children = [
                            dcc.Dropdown(
                                options = [
                                    'Top 10 NFT', 
                                    'Asset Category',
                                    'Collection Slug', 
                                    'Created Year'
                                ],
                                value = 'Top 10 NFT',
                                id='transaction-choose-category',
                                style={
                                    'width':'50%'
                                }
                            ),
                            html.Div(
                                id='transaction-choose-options',
                                style = {
                                    'width':'50%'
                                },
                                children = [
                                    dcc.Dropdown(
                                        id='transaction-choose-option',
                                        options = ['None'],
                                        value = 'None'
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Br(),
                    html.Div(
                        id='transaction-choose-content'
                    )
                ]
            )
        ]
    )


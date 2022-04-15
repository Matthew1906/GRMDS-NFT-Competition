from pydoc import classname
from tkinter.ttk import Style
from dash import html, dcc

def get_layout():
    return html.Div(
        children=[
            html.H1('NFT Transactions Analysis', id='transaction-heading', className="font-semibold text-xl"),
            html.Div(
                id='transaction',
                children=[
                    html.Div(
                        className="flex items-center",
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
                                style={'width': '100%'}
                            ),
                            html.Div(
                                id='transaction-choose-options',
                                children = [
                                    dcc.Dropdown(
                                        id='transaction-choose-option',
                                        options = ['None'],
                                        value = 'None'
                                    )
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        id='transaction-choose-content',
                        children=[],
                    )
                ],
                className="flex flex-col gap-8"
            )
        ],
        className="bg-white p-8 rounded-md shadow-md col-span-7 flex flex-col gap-6"
    )


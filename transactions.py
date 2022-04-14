from dash import Dash, dcc, html, dash_table, Input, Output
from preprocessing import get_assets

app = Dash(__name__, suppress_callback_exceptions=True)

assets = get_assets()

app.layout = html.Div(
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

@app.callback(
    Output(component_id='transaction-choose-options', component_property='children'),
    Output(component_id='transaction-heading', component_property='children'),
    Input(component_id='transaction-choose-category', component_property='value')
)
def update_choose_options(category):
    return dcc.Dropdown(
        options = sorted(assets[category if category!=None else 'Asset Category'].unique()),
        value = sorted(assets[category if category!=None else 'Asset Category'].unique())[0],
        id='transaction-choose-option'
    ) if category!='Top 10 NFT' else html.Div(id='transaction-choose-option'),\
    f'Top 10 NFT Transactions based on {category}' if category!='Top 10 NFT' else 'Top 10 NFT Transactions'

@app.callback(
    Output(component_id='transaction-choose-content', component_property='children'),
    Input(component_id='transaction-choose-category', component_property='value'),
    Input(component_id='transaction-choose-option', component_property='value')
)
def update_result(category, option):
    if category == 'Top 10 NFT':
        display = assets.sort_values('Num Sales', ascending=False)[['Collection Slug','Name','Asset Category','Created Year','Num Sales']].head(10)
    else:  
        selected = assets.loc[assets[category]==option]
        display = selected.sort_values('Num Sales', ascending=False)[['Collection Slug','Name','Asset Category','Num Sales','Created Year']].head(10)
    return dash_table.DataTable(
        id='top-10-nft',
        data = display.to_dict('records'),
        columns = [{'id':col, 'name':col} for col in display.columns],
        style_header = {
            'textAlign':'center'
        },
        style_data = {
            'textAlign':'left'
        }
    ) 

if __name__ == "__main__":
    app.run_server(debug=True)
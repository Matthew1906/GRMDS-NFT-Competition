from dash import Dash, dcc, html, dash_table, Input, Output
from preprocessing import get_assets

app = Dash(__name__, suppress_callback_exceptions=True)

assets = get_assets()
top_10_NFT = assets.sort_values('num_sales', ascending=False)[['collection_slug','token_id','name','asset_category','created_year','num_sales']].head(10)

app.layout = html.Div(
    children=[
        html.H1('NFT Transactions Analysis'),
        html.Div(
            children = [
                html.H3("Top 10 NFT Transactions"),
                dash_table.DataTable(
                    id='top-10-nft',
                    data = top_10_NFT.to_dict('records'),
                    columns = [{'id':col, 'name':col} for col in top_10_NFT.columns]
                )                
            ]
        ),
        html.Div(
            id='transaction-choose',
            children=[
                html.H3(id='transaction-choose-heading'),
                html.Div(
                    style = {'display':'flex', 'justifyContent':'center', 'alignItems':'center'},
                    children = [
                        dcc.Dropdown(
                            options = ['asset_category', 'collection_slug', 'created_year'],
                            value = 'asset_category',
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
                html.Div(
                    id='transaction-choose-content'
                )
            ]
        )
    ]
)

@app.callback(
    Output(component_id='transaction-choose-options', component_property='children'),
    Output(component_id='transaction-choose-heading', component_property='children'),
    Input(component_id='transaction-choose-category', component_property='value')
)
def update_choose_options(category):
    return dcc.Dropdown(
        options = assets[category if category!=None else 'asset_category'].unique(),
        value = assets[category if category!=None else 'asset_category'].unique()[0],
        id='transaction-choose-option'
    ), f'Top 10 NFT Transactions based on {category}'

@app.callback(
    Output(component_id='transaction-choose-content', component_property='children'),
    Input(component_id='transaction-choose-category', component_property='value'),
    Input(component_id='transaction-choose-option', component_property='value')
)
def update_result(category, option):
    selected = assets.loc[assets[category]==option]
    display = selected.sort_values('num_sales', ascending=False)[['collection_slug','token_id','name','asset_category','num_sales','created_year']].head(10)
    return dash_table.DataTable(
        data = display.to_dict('records'),
        columns = [{'id':col, 'name':col} for col in display.columns]
    )

if __name__ == "__main__":
    app.run_server(debug=True)
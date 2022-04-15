from dash import dcc, dash_table, html, Input, Output

def get_callbacks(app, assets):
    @app.callback(
        Output(component_id='transaction-choose-options', component_property='children'),
        Output(component_id='transaction-heading', component_property='children'),
        Output(component_id='transaction-choose-category', component_property='style'),
        Output(component_id='transaction-choose-options', component_property='style'),
        Input(component_id='transaction-choose-category', component_property='value')
    )
    def update_choose_options(category):
        return dcc.Dropdown(
            options = sorted(assets[category if category!=None else 'Asset Category'].unique()),
            value = sorted(assets[category if category!=None else 'Asset Category'].unique())[0],
            id='transaction-choose-option',
        ) if category!='Top 10 NFT' else html.Div(id='transaction-choose-option'),\
        f'Top 10 NFT Transactions based on {category}' if category!='Top 10 NFT' else 'Top 10 NFT Transactions',\
        {'width':'95%'} if category!='Top 10 NFT' else {'width':'100%'},\
        {'width':'50%'} if category!='Top 10 NFT' else {'display':'none'}

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
        display.rename(columns={"Asset Category": "Category", "Num Sales":"Sales"}, inplace=True)

        return dash_table.DataTable(
            id='top-10-nft',
            data = display.to_dict('records'),
            columns = [{'id':col, 'name':col} for col in display.columns],
            style_header = {
                'textAlign':'center'
            },
            style_data = {
                'textAlign':'left',
                'fontSize': 14,
            },
            style_table = {
                'overflowX': 'auto'
            }
        ) 
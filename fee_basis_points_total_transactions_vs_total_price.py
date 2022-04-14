from cProfile import label
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from preprocessing import get_assets

app = Dash(__name__, suppress_callback_exceptions=True)

assets = get_assets()
assets_sold = assets[assets['last_sale_created_date'].notna()]
fig = px.scatter(assets_sold['last_sale_total_price'], 
                assets_sold['asset_contract_dev_seller_fee_basis_points'],
                labels={'index':"Last Sale Created Date",
                        'x':'Asset Contract Dev Seller Fee Basis Points'
                },
                trendline="ols")

app.layout = html.Div(children=[
	html.H1("Fee Basis Points & Total Transactions vs. Total Price"),
	html.Div(
        dcc.Graph(id="scat_plt", figure=fig)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
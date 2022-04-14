from cProfile import label
import plotly.express as px
import plotly.subplots as sp
from dash import Dash, dcc, html, Input, Output
from preprocessing import get_assets

app = Dash(__name__, suppress_callback_exceptions=True)

assets = get_assets()
assets_sold = assets[assets['last_sale_created_date'].notna()]

figure1 = px.scatter(assets_sold['last_sale_total_price'], 
                assets_sold['asset_contract_dev_seller_fee_basis_points'],
                color_discrete_sequence=["black"],
                labels={'index':"Last Sale Created Date",
                        'x':'Asset Contract Dev Seller Fee Basis Points'
                },
                trendline="ols",
                trendline_color_override="black")

figure2 = px.scatter(assets_sold['last_sale_total_price'], 
                assets_sold['asset_contract_dev_seller_fee_basis_points'],
                labels={'index':"Last Sale Created Date",
                        'x':'Asset Contract Dev Seller Fee Basis Points'
                },
                trendline="ols")


# figure1_traces = []
# figure2_traces = []
# for trace in range(len(figure1["data"])):
#     figure1_traces.append(figure1["data"][trace])
# for trace in range(len(figure2["data"])):
#     figure2_traces.append(figure2["data"][trace])

# this_figure = sp.make_subplots(rows=1, cols=2) 

# # Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot
# for traces in figure1_traces:
#     this_figure.append_trace(traces, row=1, col=1)
# for traces in figure2_traces:
#     this_figure.append_trace(traces, row=1, col=2)

app.layout = html.Div(children=[
	html.H1("Fee Basis Points & Total Transactions vs. Total Price"),
	html.Div(
        dcc.Graph(id="scat_plt", figure=figure1)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
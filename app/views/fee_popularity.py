import plotly.express as px
from dash import dcc, html
from plotly.subplots import make_subplots

def get_layout(assets):
    assets_sold = assets[assets['Last Sale Created Date'].notna()]
    this_figure = make_subplots(rows=3, cols=1, subplot_titles=("Fee Basis Points vs Total Price", "Scatter plot of asset favorites and last sale total price", "Scatter plot of num sales and last sale total price"))
    figure1 = px.scatter(
        assets_sold, 
        x='Last Sale Total Price', 
        y='Asset Contract Dev Seller Fee Basis Points',
        color_discrete_sequence=["red"],
        trendline="ols",
        trendline_color_override="red"
    )

    figure2 = px.scatter(
        assets, 
        x='Last Sale Total Price',
        y='Asset Favorites',
        color_discrete_sequence=["blue"],
        trendline='ols',
        trendline_color_override="blue"
    )

    figure3 = px.scatter(
        assets, 
        x='Last Sale Total Price',
        y='Num Sales', 
        color_discrete_sequence=["orange"],
        trendline='ols',
        trendline_color_override="orange"
    )

    figure1_traces = []
    figure2_traces = []
    figure3_traces = []

    for trace in range(len(figure1["data"])):
        figure1_traces.append(figure1["data"][trace])
        
    for trace in range(len(figure2["data"])):
        figure2_traces.append(figure2["data"][trace])

    for trace in range(len(figure3["data"])):
        figure3_traces.append(figure3["data"][trace])

    for traces in figure1_traces:
        this_figure.append_trace(traces, row=1, col=1)

    for traces in figure2_traces:
        this_figure.append_trace(traces, row=2, col=1)
        
    for traces in figure3_traces:
        this_figure.append_trace(traces, row=3, col=1)

    this_figure.update_layout(height=1000, showlegend=False)

    this_figure.update_xaxes(title_text='Last Sale Total Price', row=1, col=1)
    this_figure.update_xaxes(title_text='Last Sale Total Price', row=2, col=1)
    this_figure.update_xaxes(title_text='Last Sale Total Price', row=3, col=1)

    this_figure.update_yaxes(title_text='Asset Contract Dev Seller Basis Points', row=1, col=1)
    this_figure.update_yaxes(title_text='Asset Favorites', row=2, col=1)
    this_figure.update_yaxes(title_text='Num Sales', row=3, col=1)

    return html.Div(children=[
        html.H1('How popularity & total transactions affect an NFT price'),
        dcc.Graph(
            figure = this_figure
        )
    ])
import plotly.express as px
from dash import dcc, html
from plotly.subplots import make_subplots

def get_layout(assets):
    assets_sold = assets[assets['Last Sale Created Date'].notna()]
    this_figure = make_subplots(rows=1, cols=3, subplot_titles=("Fee Basis Points vs Last Sale Total Price", "Asset Favorites vs Last Sale Total Price", "Num Sales vs Last Sale Total Price"))
    figure1 = px.scatter(
        assets_sold, 
        x='Last Sale Total Price', 
        y='Asset Contract Dev Seller Fee Basis Points',
        color_discrete_sequence=["red"],
        trendline="ols",
        trendline_color_override="red"
    )

    # figure1.update_layout(yaxis=dict(range=[0,1000]))

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
        this_figure.append_trace(traces, row=1, col=2)
        
    for traces in figure3_traces:
        this_figure.append_trace(traces, row=1, col=3)

    this_figure.update_layout(height=500, showlegend=False)

    this_figure.update_xaxes(title_text='Last Sale Total Price', row=1, col=1)
    this_figure.update_xaxes(title_text='Last Sale Total Price', row=1, col=2)
    this_figure.update_xaxes(title_text='Last Sale Total Price', row=1, col=3)

    this_figure.update_yaxes(title_text='Asset Contract Dev Seller Basis Points', row=1, col=1, range=[-50,1050])
    this_figure.update_yaxes(title_text='Asset Favorites', row=1, col=2)
    this_figure.update_yaxes(title_text='Num Sales', row=1, col=3)

    return html.Div(children=[
        html.H1('How popularity & total transactions affect an NFT price', className="font-semibold text-xl"),
        dcc.Graph(
            figure = this_figure
        )
    ],
    className="bg-white p-8 rounded-md shadow-md col-span-12")
    
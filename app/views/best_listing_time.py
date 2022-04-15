import plotly.express as px
from dash import html, dcc

def get_layout(best_listing):
    '''Get Layout for Best Listing Time'''
    fig = px.bar(
        data_frame = best_listing, 
        x = 'duration_range', 
        y = 'count',
        color = 'duration_range', 
        text = 'count',
        labels = {
            "duration_range":"Duration",
            "count":"No. of events observed"
        }
    )
    fig.update_traces(
        textfont_size = 12, 
        textposition = "outside", 
        cliponaxis = False
    )
    fig.update_layout(showlegend = False)
    return html.Div(
        children = [
            html.Div(
                children=[
                    html.H1(
                        children = ["Best Listing Duration"], 
                        className = "font-semibold text-xl"
                    ),
                    dcc.Graph(figure = fig)
                ]
            )
        ],
        className = "bg-white p-8 rounded-md shadow-md flex flex-col justify-between col-span-4"
    )
    
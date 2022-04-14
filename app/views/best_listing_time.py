import dash_bootstrap_components as dbc
import plotly.express as px
from dash import html, dcc

def get_layout(best_listing):
    fig = px.bar(
        best_listing, 
        x='duration_range', y='count',
        color='duration_range', text='count',
        title='<b>Events observed based on Duration</b>',
        labels={
            "duration_range": "<b>Duration</b>",
            "count": "<b>No. of events observed</b>"
        }
    )
    fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
    fig.update_layout(showlegend=False)
    return dbc.Container(children=[
        html.Div(children=[
            html.H1("Best Listing Duration"),
            dcc.Graph(figure=fig, style={
                'width': '50%',
                'height': '500px'
            })
        ], 
            style={
                'font-family': 'Poppins'
            }
        )
    ], className="p-5")
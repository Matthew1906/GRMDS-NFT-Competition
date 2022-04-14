import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

best_listing = pd.read_csv('./cleaned-datasets/best_listing.csv')

import plotly.express as px

fig = px.bar(best_listing, x='duration_range', y='count',
            color='duration_range', text='count',
            title='<b>Events observed based on Duration</b>',
            labels={
                "duration_range": "<b>Duration</b>",
                "count": "<b>No. of events observed</b>"
            })
fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
fig.update_layout(showlegend=False)

from dash import Dash, html, dcc
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(children=[
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

if __name__ == "__main__":
    app.run_server(debug=True)
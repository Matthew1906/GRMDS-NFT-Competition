import pandas as pd
import numpy as np

best_listing = pd.read_csv('./cleaned-datasets/best_listing.csv')

from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)
fig = px.bar(best_listing, x='duration_range', y='count',
            color='duration_range', text='count',
            title='<b>Events observed based on Duration</b>',
            labels={
                "duration_range": "<b>Duration</b>",
                "count": "<b>No. of events observed</b>"
            })
fig.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
fig.update_layout(showlegend=False)

app.layout = html.Div(children=[
    html.H1("Best Listing Duration"),
    dcc.Graph(figure=fig, style={
        'width': '50%',
        'height': '500px'
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)
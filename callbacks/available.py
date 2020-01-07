import numpy as np

from dash.dependencies import Input, Output, State
from main import app


@app.callback(
    Output("hidden_data", "value"),
    [
        Input("switches_input", "value"),
    ]
)
def update_hidden_data(switches_value):
    data = dict()
    data['available'] = switches_value
    chosen_beers = np.random.choice(switches_value, 2, replace=False)
    data['start_left'] = chosen_beers[0]
    data['start_right'] = chosen_beers[1]
    return data


# @app.callback(
#     Output("pbl_data", "value"),
#     [
#         Input("url", "pathname")
#
#     ],
#     [
#         State("hidden_data", "value")
#     ]
# )
# def pbl_update(pathname, data):
#     if pathname == '/selection':
#
#         return data

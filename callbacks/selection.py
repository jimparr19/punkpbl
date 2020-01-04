from dash.dependencies import Input, Output, State
from app import app
from config import punk_df

import numpy as np


@app.callback(
    [
        Output("left_image", "src"),
        Output("left_card_title", "children"),
        Output("left_description", "children")
    ],
    [
        Input("right_button", "n_clicks")],
    [
        State("hidden_data", "value")
    ]
)
def on_left_selection(n_clicks, data):
    if n_clicks:
        choice = np.random.choice(data['punk_index'])
    else:
        choice = 0
    return punk_df.loc[choice, 'image_url'], punk_df.loc[choice, 'name'], punk_df.loc[choice, 'tagline']


@app.callback(
    [
        Output("right_image", "src"),
        Output("right_card_title", "children"),
        Output("right_description", "children")
    ],
    [
        Input("left_button", "n_clicks")

    ],
    [
        State("hidden_data", "value")
    ]
)
def on_right_selection(n_clicks, data):
    if n_clicks:
        choice = np.random.choice(data['punk_index'])
    else:
        choice = 1
    return punk_df.loc[choice, 'image_url'], punk_df.loc[choice, 'name'], punk_df.loc[choice, 'tagline']

import copy

import numpy as np

from dash.dependencies import Input, Output, State
from main import app
from config import punk_df


@app.callback(
    [
        Output("preference_data", "value"),
        Output("left_button", "disabled"),
        Output("right_button", "disabled")
    ],
    [

        Input("left_button", "n_clicks_timestamp"),
        Input("right_button", "n_clicks_timestamp")

    ],
    [
        State("left_card_title", "children"),
        State("right_card_title", "children"),
        State("preference_data", "value"),
        State("hidden_data", "value")
    ]
)
def pbl_update(n_clicks_left, n_clicks_right, left_beer_name, right_beer_name,
               previous_preference_data, available_data):
    # get indexes used
    left_index = int(punk_df[punk_df.name == left_beer_name].index.values)
    right_index = int(punk_df[punk_df.name == right_beer_name].index.values)

    n_clicks_left = n_clicks_left if n_clicks_left is not None else 0
    n_clicks_right = n_clicks_right if n_clicks_right is not None else 0

    if n_clicks_left > n_clicks_right:
        preference = [left_index, right_index]
        choice = 'left'
    elif n_clicks_right > n_clicks_left:
        preference = [right_index, left_index]
        choice = 'right'
    if previous_preference_data:
        preference_data = copy.deepcopy(previous_preference_data)
        preference_data['preferences'].append(preference)
        preference_data['tasted'] = list(set(previous_preference_data['tasted'] + preference))
    else:
        preference_data = dict()
        preference_data['preferences'] = [preference]
        preference_data['tasted'] = preference

    preference_data['not_tasted'] = list(set(available_data['available']) - set(preference_data['tasted']))
    preference_data['choice'] = choice
    preference_data['right'] = right_index
    preference_data['left'] = left_index

    if len(preference_data['not_tasted']) > 0:
        return preference_data, False, False
    else:
        return preference_data, True, True


@app.callback(
    [
        Output("left_image", "src"),
        Output("left_card_title", "children"),
        Output("left_description", "children")
    ],
    [
        Input("preference_data", "value")
    ]
)
def update_left_beer(preference_data):
    if (preference_data['choice'] == 'right') & (len(preference_data['not_tasted']) > 0):
        if len(preference_data['not_tasted']) > 1:
            next_choice = np.random.choice(preference_data['not_tasted'])
        else:
            next_choice = preference_data['not_tasted'][0]
        return punk_df.loc[next_choice, 'image_url'], punk_df.loc[next_choice, 'name'], punk_df.loc[
            next_choice, 'tagline']
    else:
        return punk_df.loc[preference_data['left'], 'image_url'], punk_df.loc[preference_data['left'], 'name'], \
               punk_df.loc[preference_data['left'], 'tagline']


@app.callback(
    [
        Output("right_image", "src"),
        Output("right_card_title", "children"),
        Output("right_description", "children")
    ],
    [
        Input("preference_data", "value")

    ]
)
def update_right_beer(preference_data):
    if (preference_data['choice'] == 'left') & (len(preference_data['not_tasted']) > 0):
        if len(preference_data['not_tasted']) > 1:
            next_choice = np.random.choice(preference_data['not_tasted'])
        else:
            next_choice = preference_data['not_tasted'][0]
        return punk_df.loc[next_choice, 'image_url'], punk_df.loc[next_choice, 'name'], punk_df.loc[
            next_choice, 'tagline']
    else:
        return punk_df.loc[preference_data['right'], 'image_url'], punk_df.loc[preference_data['right'], 'name'], \
               punk_df.loc[
                   preference_data['right'], 'tagline']

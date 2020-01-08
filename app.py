import pandas as pd
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

from main import app
from layout.main import main_layout
from layout.splash import splash_layout
from layout.available import available_layout
from layout.selection import get_selection_layout
from layout.recommendation import get_recommendation_layout

from pypbl.elicitation import BayesPreference
from pypbl.priors import Normal

from config import punk_df
from config import features

# from callbacks import splash  # noqa
from callbacks import available  # noqa
from callbacks import selection  # noqa

app.layout = main_layout
server = app.server


# update page based on url
@app.callback(
    Output('page_content', 'children'),
    [Input('url', 'pathname')],
    [State('hidden_data', 'value'),
     State('preference_data', 'value')])
def display_page(pathname, data, preference_data):  # noqa
    if pathname == '/':
        return splash_layout
    elif pathname == '/available':
        return available_layout
    elif pathname == '/selection':
        return get_selection_layout(data)
    elif pathname == '/recommendation':
        available_beers_df = punk_df.loc[data['available'], ['name'] + features]
        available_beers_df.set_index('name', inplace=True)
        normalised_available_beers_df = (available_beers_df - available_beers_df.min()) / (
                available_beers_df.max() - available_beers_df.min())
        model = BayesPreference(data=normalised_available_beers_df)
        model.set_priors([Normal() for _ in features])
        for preference in preference_data['preferences']:
            model.add_strict_preference(punk_df.loc[preference[0], 'name'], punk_df.loc[preference[1], 'name'])
        model.infer_weights()
        # table for tasted beers
        tasted_table = model.rank()
        tasted_table['beer'] = tasted_table.index.values

        # table for all beers
        all_beers_df = punk_df.loc[:, ['name'] + features]
        all_beers_df.set_index('name', inplace=True)
        normalised_all_beers_df = (all_beers_df - available_beers_df.min()) / (
                    available_beers_df.max() - available_beers_df.min())
        utilities = [model.weights.dot(row.values) for i, row in normalised_all_beers_df.iterrows()]
        rank_df = pd.DataFrame(utilities, index=normalised_all_beers_df.index.values, columns=['utility'])
        table = rank_df.sort_values(by='utility', ascending=False)
        table['beer'] = table.index.values
        table['abv'] = all_beers_df.loc[table.index, 'abv'].div(100).values
        table['color'] = all_beers_df.loc[table.index, 'ebc'].values
        table['tasted'] = ["yes" if (beer in tasted_table.index) else "no" for beer in table.index]
        cols = ['beer', 'utility', 'tasted', 'abv', 'color']
        table = table[cols]
        return get_recommendation_layout(tasted_table, table)


# update navbar items based on page
@app.callback(
    Output('nav-items', 'children'),
    [Input('url', 'pathname')])
def change_navbar(pathname):  # noqa
    if pathname == '/':
        return []
    elif pathname == '/available':
        navbar_items = [
            dbc.Col(dbc.NavLink("Available", id='available-link', href="available", className='nav_link active')),
            dbc.Col(dbc.NavLink("Selection", id='selection-link', href="selection", className='nav_link')),
            dbc.Col(
                dbc.NavLink("Recommendation", id='recommendation-link', href="recommendation", className='nav_link')
            ),
        ]
    elif pathname == '/selection':
        navbar_items = [
            dbc.Col(dbc.NavLink("Available", id='available-link', href="available", className='nav_link')),
            dbc.Col(dbc.NavLink("Selection", id='selection-link', href="selection", className='nav_link active')),
            dbc.Col(
                dbc.NavLink("Recommendation", id='recommendation-link', href="recommendation", className='nav_link')
            ),
        ]
    elif pathname == '/recommendation':
        navbar_items = [
            dbc.Col(dbc.NavLink("Available", id='available-link', href="available", className='nav_link')),
            dbc.Col(dbc.NavLink("Selection", id='selection-link', href="selection", className='nav_link')),
            dbc.Col(
                dbc.NavLink("Recommendation", id='recommendation-link', href="recommendation",
                            className='nav_link active')
            ),
        ]
    else:
        navbar_items = []
    return navbar_items


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)

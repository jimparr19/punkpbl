import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

from app import app
from layout.main import main_layout
from layout.splash import splash_layout
from layout.selection import selection_layout
from layout.available import available_layout

from callbacks import splash  # noqa
from callbacks import available  # noqa
from callbacks import selection  # noqa

app.layout = main_layout
server = app.server


# update page based on url
@app.callback(
    Output('page_content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):  # noqa
    if pathname == '/':
        return splash_layout
    elif pathname == '/available':
        return available_layout
    elif pathname == '/selection':
        return selection_layout


# update navbar items based on page
@app.callback(
    Output('nav-items', 'children'),
    [Input('url', 'pathname')])
def change_navbar(pathname):  # noqa
    if pathname == '/':
        return []
    elif pathname == '/available':
        navbar_items = [
            dbc.Col(dbc.NavLink("Beers", id='available-link', href="available", className='nav_link active')),
            dbc.Col(dbc.NavLink("PBL", id='selection-link', href="selection", className='nav_link')),
        ]
    elif pathname == '/selection':
        navbar_items = [
            dbc.Col(dbc.NavLink("Beers", id='available-link', href="available", className='nav_link')),
            dbc.Col(dbc.NavLink("PBL", id='selection-link', href="selection", className='nav_link active')),
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

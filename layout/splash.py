import dash_html_components as html
import dash_bootstrap_components as dbc

splash_layout = dbc.Jumbotron(
    children=[
        html.H1("Punk PBL", className="display-3"),
        html.P(
            "Punk Beer Preference Based Learning",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "Choose your favourite beer and get recommendations using preference based learning."
        ),

        dbc.Row(
            children=[
                dbc.Col(dbc.Button("Get started", id="btn_get_started", color="primary", size="lg", block=True)),
            ]
        ),
    ]
)


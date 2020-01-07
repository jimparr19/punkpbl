import dash_html_components as html
import dash_bootstrap_components as dbc

jumbotron = dbc.Jumbotron(
    children=[
        html.H1("PunkPBL", className="display-3", style={"text-align": "center"}),
        html.P(
            "Punk Preference Based Learning",
            className="lead",
            style={"text-align": "center"}
        ),
        html.Hr(className="my-2"),
        html.P(
            "Choose your favourite BrewDog beer and get recommendations using preference based learning.",
            style={"text-align": "center"}
        ),
    ]
)

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Step 1:", className="card-title"),
            html.P("Select the BrewDog beers available for tasting.")
        ]
    ), color="light", outline=True
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Step 2:", className="card-title"),
            html.P(
                "Select your preferred beer from the pairs presented."
            )
        ]
    ), color="light", outline=True
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Step 3:", className="card-title"),
            html.P(
                "View your top ranked and recommended beers."
            )
        ]
    ), color="light", outline=True
)

cards = dbc.Row([dbc.Col(first_card, md=4), dbc.Col(second_card, md=4), dbc.Col(third_card, md=4)])

get_started = dbc.Row(
    children=[
        dbc.Col(dbc.Button("Get started", id="btn_get_started", color="primary", size="lg", block=True, href="available")),
    ],
    className='mt-3 mb-3'
)

splash_layout = [jumbotron, cards, get_started]

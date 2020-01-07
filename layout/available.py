import dash_bootstrap_components as dbc

from config import punk_df
from config import available_beers

options = [{"label": punk.name, "value": punk.Index} for punk in punk_df.itertuples()]
available_beers_index = [row.Index for row in punk_df.itertuples() if row.name in available_beers]

switches = dbc.FormGroup(
    children=[
        dbc.Label("Punk availability:"),
        dbc.Checklist(
            options=options,
            value=available_beers_index,
            id="switches_input",
            switch=True,
            persistence=True,
            persistence_type='session'
        ),
    ],
)

form = dbc.Form([switches])

available_layout = [
    dbc.Row(
        children=[
            dbc.Col(
                children=[
                    form
                ],
                md=12
            )
        ],
    ),
    dbc.Row(
        children=[
            dbc.Col(
                md=9
            ),
            dbc.Col(
                children=[
                    dbc.Col(dbc.Button("Next", id="btn_to_selection", color="light", size="lg", block=True,
                                       href="selection")),
                ],
                md=3
            )
        ],
        className='mt-3 mb-3'),
]

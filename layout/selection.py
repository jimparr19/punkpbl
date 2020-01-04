import dash_html_components as html
import dash_bootstrap_components as dbc

from config import punk_df
from layout.available import available_beers_index

left_start_choice = available_beers_index[0]
right_start_choice = available_beers_index[1]

selection_layout = [
    dbc.Row(
        children=[
            dbc.Col(
                children=[
                    dbc.Card(
                        children=[
                            dbc.CardImg(
                                id='left_image',
                                src=punk_df.loc[left_start_choice, 'image_url'],
                                className='selection_img',
                                top=True,
                            ),
                            dbc.CardBody(
                                id='left_body',
                                children=[
                                    html.H4(punk_df.loc[left_start_choice, 'name'], id='left_card_title',
                                            className="card-title"),
                                    html.P(punk_df.loc[left_start_choice, 'tagline'], id='left_description',
                                           className="card-text"),
                                    dbc.Button(
                                        id='left_button',
                                        children="Select",
                                        color="primary"),
                                ]
                            ),
                        ],
                    )
                ],
                md=6,
            ),
            dbc.Col(
                children=[
                    dbc.Card(
                        children=[
                            dbc.CardImg(
                                id='right_image',
                                src=punk_df.loc[right_start_choice, 'image_url'],
                                className='selection_img',
                                top=True,
                            ),
                            dbc.CardBody(
                                id='right_body',
                                children=[
                                    html.H4(punk_df.loc[right_start_choice, 'name'], id='right_card_title',
                                            className="card-title"),
                                    html.P(punk_df.loc[right_start_choice, 'tagline'], id='right_description',
                                           className="card-text"),
                                    dbc.Button(
                                        id='right_button',
                                        children="Select",
                                        color="primary"),
                                ]
                            ),
                        ],
                    )
                ],
                md=6,
            ),
        ],
    )
]

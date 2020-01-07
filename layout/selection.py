import dash_html_components as html
import dash_bootstrap_components as dbc

from config import punk_df


def get_selection_layout(data):
    selection_layout = [
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.CardImg(
                                    id='left_image',
                                    src=punk_df.loc[data['start_left'], 'image_url'],
                                    className='selection_img',
                                    top=True,
                                ),
                                dbc.CardBody(
                                    id='left_body',
                                    children=[
                                        dbc.Button(
                                            id='left_button',
                                            children="Select",
                                            color="primary",
                                            block=True,
                                            className='mb-3'),
                                        html.H4(punk_df.loc[data['start_left'], 'name'], id='left_card_title',
                                                className="card-title"),
                                        html.P(punk_df.loc[data['start_left'], 'tagline'], id='left_description',
                                               className="card-text"),

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
                                    src=punk_df.loc[data['start_right'], 'image_url'],
                                    className='selection_img',
                                    top=True,
                                ),
                                dbc.CardBody(
                                    id='right_body',
                                    children=[
                                        dbc.Button(
                                            id='right_button',
                                            children="Select",
                                            color="primary",
                                            block=True,
                                            className='mb-3'),
                                        html.H4(punk_df.loc[data['start_right'], 'name'], id='right_card_title',
                                                className="card-title"),
                                        html.P(punk_df.loc[data['start_right'], 'tagline'], id='right_description',
                                               className="card-text"),

                                    ]
                                ),
                            ],
                        )
                    ],
                    md=6,
                ),
            ],
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    md=9
                ),
                dbc.Col(
                    children=[
                        dbc.Col(dbc.Button("Next", id="btn_to_recommendation", color="light", size="lg", block=True,
                                           href="recommendation")),
                    ],
                    md=3
                )
            ],
            className='mt-3 mb-3')
    ]
    return selection_layout

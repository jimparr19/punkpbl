import dash_table
from dash_table.Format import Format
import dash_table.FormatTemplate as FormatTemplate


def get_recommendation_layout(tasted_table, table):
    recommendation_layout = [
        dash_table.DataTable(
            id='table',
            columns=[{'id': 'beer', 'name': 'beer'},
                     {'id': 'utility', 'name': 'utility', 'type': 'numeric', 'format': Format(precision=2)},
                     {'id': 'tasted', 'name': 'tasted'},
                     {'id': 'abv', 'name': 'abv', 'type': 'numeric', 'format': FormatTemplate.percentage(1)},
                     {'id': 'color', 'name': 'color'},
                     ],
            data=table.to_dict('records'),
            style_cell_conditional=[
                {
                    'if': {'column_id': 'beer'},
                    'textAlign': 'left',
                },
            ],
            style_data_conditional=[
                {
                    'if': {
                        'column_id': 'tasted',
                        'filter_query': '{tasted} eq "yes"'
                    },
                    'backgroundColor': '#E9ECEF',
                    'fontWeight': 'bold',

                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} lt 4'
                    },
                    'backgroundColor': '#F8F753',
                    'color': '#F8F753',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 4 && {color} lt 6'
                    },
                    'backgroundColor': '#F6F513',
                    'color': '#F6F513',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 6 && {color} lt 8'
                    },
                    'backgroundColor': '#ECE61A',
                    'color': '#ECE61A',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 8 && {color} lt 12'
                    },
                    'backgroundColor': '#D5BC26',
                    'color': '#D5BC26',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 12 && {color} lt 16'
                    },
                    'backgroundColor': '#BF923B',
                    'color': '#BF923B',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 16 && {color} lt 20'
                    },
                    'backgroundColor': '#BF813A',
                    'color': '#BF813A',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 20 && {color} lt 26'
                    },
                    'backgroundColor': '#BC6733',
                    'color': '#BC6733',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 26 && {color} lt 33'
                    },
                    'backgroundColor': '#8D4C32',
                    'color': '#8D4C32',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 33 && {color} lt 39'
                    },
                    'backgroundColor': '#5D341A',
                    'color': '#5D341A',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 39 && {color} lt 47'
                    },
                    'backgroundColor': '#261716',
                    'color': '#261716',
                },
                {
                    'if': {
                        'column_id': 'color',
                        'filter_query': '{color} ge 47'
                    },
                    'backgroundColor': '#0F0B0A',
                    'color': '#0F0B0A',
                }
            ]
        )

    ]
    return recommendation_layout

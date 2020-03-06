import os
import pandas as pd
import dash_bootstrap_components as dbc

config_path = os.path.dirname(__file__)

# Style
THEME = dbc.themes.BOOTSTRAP

# Data
punk_df = pd.read_pickle(os.path.join(config_path, 'punk_df_202001181918.pickle'))

# Default beers
available_beers = [
    'Indie Pale Ale',
    'Hazy Jane',
    'Kingpin',
    'Punk IPA 2010 - Current',
    'Clockwork Tangerine',
    'Vagabond Pale ALe - Prototype Challenge',
    '5am Saint',
    'Elvis Juice V2.0 - Prototype Challenge',
    'Dead Pony Club',
]

features = ['abv', 'ibu', 'ebc', 'n_hops']

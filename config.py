import os
import pandas as pd
import dash_bootstrap_components as dbc

config_path = os.path.dirname(__file__)

# Style
THEME = dbc.themes.BOOTSTRAP

# Data
punk_df = pd.read_pickle(os.path.join(config_path, 'punk_df_201910152214.pickle'))

# Default beers
available_beers = [
    'Punk IPA 2010 - Current',
    'Dead Pony Club',
    'Elvis Juice V2.0 - Prototype Challenge',
    'Hazy Jane',
    'Indie Pale Ale',
    'Hazy Jane',
    'Clockwork Tangerine'
]

features = ['abv', 'ibu', 'ebc']

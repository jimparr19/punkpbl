import pandas as pd
import dash_bootstrap_components as dbc

# Style
THEME = dbc.themes.BOOTSTRAP

# Data
punk_df = pd.read_pickle('punk_df_201910152214.pickle')

# Default beers
available_beers = [
    'Nanny State',
    'Punk IPA 2010 - Current',
    'Dead Pony Club',
    'Elvis Juice V2.0 - Prototype Challenge',
    'Hazy Jane',
    'Lost Dog (w/Lost Abbey)',
    '5am Saint',
    'Alice Porter',
    'Indie Pale Ale'
]

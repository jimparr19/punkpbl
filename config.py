import os
import pandas as pd
import dash_bootstrap_components as dbc

config_path = os.path.dirname(__file__)

# Style
THEME = dbc.themes.BOOTSTRAP

# Data
punk_df = pd.read_pickle(os.path.join(config_path, 'punk_df_202001181918.pickle'))

# Add Lost Lager
lost_lager_df = pd.DataFrame({
    'name': ['Lost Lager'],
    'tagline': ['DRY-HOPPED PILSNER.'.capitalize()],
    'first_brewed': ['2018'],
    'description': [
        '''A pilsner that combines the light, crisp and clean lager profile provided by Weihenstephan's house yeast, with the vibrant citrus and stonefruit aromas associated with new German hop Saphir. This lager is easy-going but has subtle depths; toast, hints of spice and a zesty lime marmalade character.'''],
    'image_url': ['https://images.punkapi.com/v2/keg.png'],
    'abv': [4.7],
    'ibu': [37.0],
    'target_fg': [1006.0],
    'target_og': [1042.0],
    'ebc': [5],
    'srm': [3.0],
    'ph': [4.4],
    'attenuation_level': [86.0],
    'volume': [{'value': 20, 'unit': 'litres'}],
    'boil_volume': [{'value': 25, 'unit': 'litres'}],
    'method': [{'mash_temp': [{'temp': {'value': 65, 'unit': 'celsius'}, 'duration': 65}],
                'fermentation': {'temp': {'value': 11, 'unit': 'celsius'}},
                'twist': 'Amyloglucosidase: 1g at end'}],
    'ingredients': [{'malt': [{'name': 'Pilsner Malt', 'amount': {'value': 3.36, 'unit': 'kilograms'}},
                              {'name': 'Carapils Malt', 'amount': {'value': 0.24, 'unit': 'kilograms'}}],
                     'hops': [{'name': 'Hallertauer Taurus', 'amount': {'value': 8, 'unit': 'grams'}, 'add': '60',
                               'attribute': 'Bittering'},
                              {'name': 'Select Spalter', 'amount': {'value': 15, 'unit': 'grams'}, 'add': '20',
                               'attribute': 'Flavour'},
                              {'name': 'Select Spalter', 'amount': {'value': 15, 'unit': 'grams'}, 'add': '10',
                               'attribute': 'Aroma'},
                              {'name': 'Saphir', 'amount': {'value': 30, 'unit': 'grams'}, 'add': '0',
                               'attribute': 'Aroma'},
                              {'name': 'Saphir', 'amount': {'value': 30, 'unit': 'grams'}, 'add': 'Dry Hop',
                               'attribute': 'Aroma'}],
                     'yeast': 'W34/70'}],
    'food_pairing': [['Vietnamese Pho', 'Buffalo Chicken Wings', 'Sashimi']],
    'brewers_tips': [''],
    'contributed_by': ['Jim Parr jimparr19@googlemail.com'],
    'n_malt': [2],
    'n_hops': [5]
})
punk_df = punk_df.append(lost_lager_df, ignore_index=True, sort=True)

# Add Zombie Cake
zombie_cake_df = pd.DataFrame({
    'name': ['Zombie Cake'],
    'tagline': ['Chocolate Praline Porter.'],
    'first_brewed': ['2018'],
    'description': [
        'Dark forces are at work in this devilishly good Praline Porter. Toffee and chocolate unite and come a-knocking. Open up to layers of smooth roasty character, with notes of vanilla, mellow coffee and a subtle nuttiness. And a bittersweet cliff-hanger finale. Zombie Cake - Bittersweet, engaging and rewarding.'],
    'image_url': ['https://images.punkapi.com/v2/keg.png'],
    'abv': [5.0],
    'ibu': [25.0],
    'target_fg': [1020.0],
    'target_og': [1062.0],
    'ebc': [90],
    'srm': [46.0],
    'ph': [4.2],
    'attenuation_level': [68.0],
    'volume': [{'value': 20, 'unit': 'litres'}],
    'boil_volume': [{'value': 25, 'unit': 'litres'}],
    'method': [{'mash_temp': [{'temp': {'value': 65, 'unit': 'celsius'}, 'duration': 45}],
                'fermentation': {'temp': {'value': 19, 'unit': 'celsius'}},
                'twist': 'Vanilla Extract: 65g at FV, Milk Sugars: 360g, Honey: 240g in whirlpool'}],
    'ingredients': [{'malt': [{'name': 'Pale Ale', 'amount': {'value': 3.12, 'unit': 'kilograms'}},
                              {'name': 'Caramalt', 'amount': {'value': 0.84, 'unit': 'kilograms'}},
                              {'name': 'Simpsons T50', 'amount': {'value': 0.36, 'unit': 'kilograms'}},
                              {'name': 'Brown Malt', 'amount': {'value': 0.48, 'unit': 'kilograms'}},
                              {'name': 'Carafa Special Type 3', 'amount': {'value': 0.12, 'unit': 'kilograms'}}],
                     'hops': [{'name': 'Amarillo', 'amount': {'value': 6, 'unit': 'grams'}, 'add': '60',
                               'attribute': 'Bittering'},
                              {'name': 'Bramling Cross', 'amount': {'value': 20, 'unit': 'grams'}, 'add': '30',
                               'attribute': 'Flavour'},
                              {'name': 'Amarillo', 'amount': {'value': 4, 'unit': 'grams'}, 'add': '30',
                               'attribute': 'Flavour'}],
                     'yeast': 'Wyeast 1272'}],
    'food_pairing': [['Mimolette', 'Almond Milk Pudding', 'Pumpkin Cheesecake']],
    'brewers_tips': [''],
    'contributed_by': ['Jim Parr jimparr19@googlemail.com'],
    'n_malt': [5],
    'n_hops': [3]
})
punk_df = punk_df.append(zombie_cake_df, ignore_index=True, sort=True)

# Add QUENCH QUAKE
quench_quake_df = pd.DataFrame({
    'name': ['Quench Quake'],
    'tagline': ['GRAPEFRUIT AND TANGERINE SOUR.'.capitalize()],
    'first_brewed': ['2018'],
    'description': [
        '''A session strength sour ale infused with grapefruit and tangerine. A straightforward, easy-going introduction to sour beer'''],
    'image_url': ['https://images.punkapi.com/v2/keg.png'],
    'abv': [4.6],
    'ibu': [10.0],
    'target_fg': [1008.0],
    'target_og': [1044.0],
    'ebc': [10],
    'srm': [5.0],
    'ph': [3.3],
    'attenuation_level': [82.0],
    'volume': [{'value': 20, 'unit': 'litres'}],
    'boil_volume': [{'value': 25, 'unit': 'litres'}],
    'method': [{'mash_temp': [{'temp': {'value': 53, 'unit': 'celsius'}, 'duration': 25}],
                'fermentation': {'temp': {'value': 21, 'unit': 'celsius'}},
                'twist': 'Grapefruit Juice: 100g at FV, White Grapefruit Juice: 100g at FV, Tangerine Juice: 150g at FV, Lactic Acid: 50g at end, Malic Acid: 10g at end, Citric Acid Poweder: 40g at end'}],
    'ingredients': [{'malt': [{'name': 'Pale Ale', 'amount': {'value': 2.52, 'unit': 'kilograms'}},
                              {'name': 'Wheat Malt', 'amount': {'value': 1.2, 'unit': 'kilograms'}}],
                     'hops': [{'name': 'Perle', 'amount': {'value': 8, 'unit': 'grams'}, 'add': '60',
                               'attribute': 'Bittering'}],
                     'yeast': 'Wyeast 1272'}],
    'food_pairing': [['Barrel-Aged Feta Salad', 'Avocado Toast', 'Spiced Orange Tart']],
    'brewers_tips': [''],
    'contributed_by': ['Jim Parr jimparr19@googlemail.com'],
    'n_malt': [2],
    'n_hops': [1]
})
punk_df = punk_df.append(quench_quake_df, ignore_index=True, sort=True)

# Others to add
# HOP FICTION
# PARADOX ISLAY
# JET BLACK HEART
# JACK HAMMER
# BOUNTY HUNTER

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
    'Lost Lager',
    'Zombie Cake',
]

features = ['abv', 'ibu', 'ebc', 'n_hops', 'ph']

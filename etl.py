import requests
import pandas as pd

url = 'https://api.punkapi.com/v2/beers'


def get_beer_query(id):
    r = requests.get('{}/{}'.format(url, id))
    return r


def get_punk_df():
    punk_df = pd.DataFrame()
    id = 1
    while True:
        print('Getting punk beer data with id {}.'.format(id))
        punk_response = get_beer_query(id)
        if punk_response.status_code == 200:
            beer_data = punk_response.json()
            beer_df = pd.DataFrame(beer_data)
            punk_df = punk_df.append(beer_df, ignore_index=True)
            id += 1
        else:
            print('No punk beer found with id {}.'.format(id))
            break
    return punk_df


def clean_data(df):
    parameters = ['abv', 'ibu', 'target_fg', 'srm', 'ph']
    df = df[df.ph < 10]
    df = df[df.ibu < 100]
    df = df[df.srm < 100]
    df = df[df.target_fg < 1030]
    # # only those that have images
    # df = df[df.image_url.apply(lambda x: x is not None)]
    # replace any missing images with default keg
    df.image_url.fillna(value='https://images.punkapi.com/v2/keg.png', inplace=True)
    # only those that have unique parameter values
    df = df.loc[df.loc[:, parameters].drop_duplicates().index]
    # # only those that have branded images
    # df = df.loc[df.image_url != 'https://images.punkapi.com/v2/keg.png']
    return pd.DataFrame.copy(df, deep=True)


def add_features(df):
    df['n_malt'] = df.ingredients.apply(lambda x: len(x['malt']))
    df['n_hops'] = df.ingredients.apply(lambda x: len(x['hops']))
    return df


if __name__ == '__main__':
    punk_df = get_punk_df()
    punk_df_with_features = add_features(punk_df)
    punk_df_clean = clean_data(punk_df_with_features)
    unique_id = pd.datetime.now().strftime('%Y%m%d%H%M')
    punk_df_clean.to_pickle('punk_df_{}.pickle'.format(unique_id))

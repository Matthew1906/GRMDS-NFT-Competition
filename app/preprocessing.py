import pandas as pd

def get_assets():
    ''' Convert the data types of the assets dataset'''
    assets = pd.read_csv('./app/models/cleaned-datasets/cleaned_assets.csv')
    # convert timestamps/datetime
    timestamps = ['last_sale_transaction_timestamp', 'last_sale_event_timestamp', 'last_sale_created_date', 'asset_contract_created_date']
    for timestamp in timestamps:
        assets[timestamp] = pd.to_datetime(assets[timestamp], format = '%Y-%m-%dT%H:%M:%S')
    # Convert categorical string
    assets['asset_category'] = assets['asset_category'].astype('category')
    # Convert numerical strings into numerical datatypes
    assets['last_sale_total_price'] = assets['last_sale_total_price'].astype('float64')
    assets['asset_favorites'] = assets['asset_favorites'].astype('int64')
    # Adding year created in assets dataframe
    assets['created_year'] = assets['asset_contract_created_date'].dt.year
    # Drop Unnecessary column
    assets.drop('token_id', axis = 'columns', inplace = True)
    # Rename columns 
    assets.columns = assets.columns.str.replace("_", " ")
    assets.columns = assets.columns.str.title()
    return assets

def get_events():
    '''Convert the data types of the events dataset'''
    events = pd.read_csv('./app/models/cleaned-datasets/cleaned_events.csv')
    # Listing all necessary changes
    timestamps = ['listing_time', 'created_date']
    categories = ['event_type', 'auction_type']
    numerics = ['total_price', 'ending_price', 'starting_price']
    # Convert datetime
    for timestamp in timestamps:
        events[timestamp] = pd.to_datetime(events[timestamp], format = '%Y-%m-%dT%H:%M:%S')
    # Convert categorical data
    events[categories] = events[categories].astype('category')
    # Convert numerical strings
    events[numerics] = events[numerics].astype('float64')
    events.columns = events.columns.str.replace("_", " ")
    events.columns = events.columns.str.title()
    return events

def get_collections():
    collections = pd.read_csv("./app/models/cleaned-datasets/cleaned_collections.csv")
    collections['created_date'] = pd.to_datetime(collections['created_date'], format = '%Y-%m-%dT%H:%M:%S')
    collections.columns = collections.columns.str.replace("_", " ")
    collections.columns = collections.columns.str.title()
    return collections

def get_listings():
    return pd.read_csv('./app/models/cleaned-datasets/best_listing.csv')
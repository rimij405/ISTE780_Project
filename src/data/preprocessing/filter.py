# filter.py
import logging
import pandas as pd
from ...data import *
from . import WALMART_FIELDS, EMPTY_FIELDS

def remove_features(df):
    """
    Filter data frame of empty and Walmart specific features.
    """
    # Get the logger
    logger = logging.getLogger(__name__)
    logger.info(f"Filtering dataframe of shape: {df.shape}.")
    
    # Get features to remove.
    features = WALMART_FIELDS + EMPTY_FIELDS
    
    # Drop the features.
    logger.info(f"Dropping features from data frame...: {features}")
    df_clean = df.drop(columns=features)
    return df_clean
    
    
def remove_bad_prices(df):
    """
    Filter data frame of bad list prices.
    """
    # Get the logger
    logger = logging.getLogger(__name__)
    logger.info(f"Filtering dataframe of shape: {df.shape}.")
    
    # Filter for List Price == 0.00
    logger.info(f"Dropping invalid prices from dataframe...")
    mask = (df['List Price'] == 0)
    num_free = df[mask].shape[0]

    # Filter out the free items.
    df_clean = df[~mask]
    num_cost = df_clean.shape[0]

    # Print info
    logger.info(f'There are {num_free} records that are listed as free.')
    logger.info(f'There are {num_cost} records that have a price > $0.00')
    logger.info(f'Shape of filtered dataframe: {df_clean.shape}')
    
    # Return filtered dataframe.
    return df_clean
    

    
    
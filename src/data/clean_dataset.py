# clean_dataset.py

import click
import logging
import os
import pandas as pd

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """Clean the dataset.
    """    
    # Get the logger.
    logger = logging.getLogger(__name__)
    
    # Raw dataset.
    df = read_data(logger, input_filepath)
    
    # Walmart-specific fields to remove.
    walmart_specific_fields = [
        'Uniq Id',
        'Product Url',
        'Item Number',
        'Gtin',    
        'Available',
    ]

    # Empty fields to remove.
    empty_fields = [
        'Package Size',
        'Postal Code',
    ]

    # Features to remove
    features = walmart_specific_fields + empty_fields
    
    # Clean the data.
    df = clean_data(logger, df, features)
    
    # Save the data.
    save_data(logger, df, output_filepath)
     
    
def read_data(logger, input_filepath):
    logger.info('Reading data from {v1}'.format(v1=input_filepath))
    return pd.read_csv(input_filepath)

def clean_data(logger, df_raw, features):

    # Remove the specified columns from the dataframe.
    df_clean = df_raw.drop(columns=features)
    
        # Filter for List Price == 0.00
    mask = (df_clean['List Price'] == 0)
    num_free = df_clean[mask].shape[0]

    # Filter out the free items.
    df_clean = df_clean[~mask]
    num_cost = df_clean.shape[0]

    # logger.info info
    logger.info('There are {v1} records that are listed as free.'.format(v1=num_free))
    logger.info('There are {v1} records that have a price > $0.00'.format(v1=num_cost))
    logger.info('Shape of filtered dataframe: {v1}'.format(v1=df_clean.shape))
    df_clean.head()
        
    return df_clean

def save_data(logger, df_clean, output_filepath):
    # Target directory
    logger.info('Saving file to "{v1}".'.format(v1=output_filepath))

    # Save the file.
    df_clean.to_csv(output_filepath)
    logger.info("File saved.")

# If main...
if __name__ == '__main__': 
    # Prepare the logging format and level.
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    # Run main.
    main()
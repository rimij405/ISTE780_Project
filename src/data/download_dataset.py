# download_dataset.py
# ---
# Downloads the raw dataset from the Kaggle API
# and moves the resulting zipfile into the output filepath.
import click
import logging
import os
from shutil import move
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    """ Runs data download scripts to get dataset from Kaggle
        and place into the data/raw folder.
    """
    download(output_filepath)
    
def download(output_filepath):    
    """ Runs data download scripts to get dataset from Kaggle
        and place into the data/raw folder.
    """
    # Get the logger.
    logger = logging.getLogger(__name__)
    
    # Check if output file exists.
    if(os.path.isfile(output_filepath)):
        logger.warning("Dataset already exists at specified location")
        return
    
    # Load envvars.
    load_envvars(logger)
    
    # Authenticate
    api = authenticate(logger)
        
    # Download the kaggle dataset.
    # https://technowhisp.com/kaggle-api-python-documentation/
    logger.info('Downloading dataset...')
    api.dataset_download_files('promptcloud/walmart-product-data-2019', quiet=False, unzip=False)
    # kaggle datasets download -d promptcloud/walmart-product-data-2019
    
    # Move to the next location.
    move_dataset(logger, "walmart-product-data-2019.zip", output_filepath)
    
def move_dataset(logger, input_filepath, output_filepath):
    """Move dataset file to the output directory location.

    :param logger: Logger.
    :param input_filepath: Input filepath (relative to project root).
    :param output_filepath: Output directory path.
    """
    logger.info('Looking for dataset at "' + input_filepath + '" ...')
    
    # Get the file.
    source_path = input_filepath
    
    # Check if source file exists.
    if(not os.path.isfile(source_path)):
        logger.error("Cannot find dataset at specified path.")
        return
    
    logger.info("Found dataset.")
    
    target_path = Path(output_filepath)
    logger.info('Moving dataset into output directory "' + str(target_path) + '" ...')
    
    # Move the dataset, overwriting if it exists.
    move(str(source_path), str(target_path))
    
    logger.info("Moved dataset.")
    
def load_envvars(logger):
    """ Load the environment variables for Kaggle authentication.
    """    
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    logger.info("Loading envvars...")
    load_dotenv(find_dotenv())
    logger.info("Done loading envvars.")
    
def authenticate(logger):
    """ Authenticate to the KaggleAPI.
    """    
    # Authenticate.
    logger.info("Authenticating to the Kaggle API...")
    api = KaggleApi()
    api.authenticate()
    logger.info("Done authenticating to the Kaggle API.")
    return api

# Executes when 'main' is set.
if __name__ == '__main__':
    # Prepare the logging format and level.
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
        
    # Execute the main function.
    main()
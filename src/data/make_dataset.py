# -*- coding: utf-8 -*-
import click
import logging
import os
from shutil import move
from pathlib import Path
from zipfile import ZipFile
from dotenv import find_dotenv, load_dotenv

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    # Get the logger.
    logger = logging.getLogger(__name__)
    
    # Load the envvars.
    load_envvars(logger)
    
    # Check if dataset exists to be unpacked
    if not dataset_exists(logger, input_filepath):
        return
        
    # Attempt to unpack the zipfile.
    unpack_dataset(logger, input_filepath, output_filepath)    

def load_envvars(logger):
    """ Load the environment variables for Kaggle authentication.
    """    
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    logger.info("Loading envvars...")
    load_dotenv(find_dotenv())
    logger.info("Done loading envvars.")
    
def dataset_exists(logger, input_filepath):
    """Determine if the zipped dataset file exists.
    """
    # Check if file exists.
    if(os.path.exists(str(input_filepath))):
        logger.info("Dataset exists.")
        return True
    else:
        logger.error("Missing dataset to unpack.")
        return False
    
def unpack_dataset(logger, input_filepath, output_filepath):
    """Unpack dataset from its zipfile.
    """
    member_path = "home/sdf/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv"
    
    logger.info('Extracting "' + member_path + '" from "' + input_filepath + '" to "' + output_filepath + '"')
    
    # Reference: https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/
    with ZipFile(input_filepath, 'r') as zf:
        zf.extract(member_path, output_filepath)
        
    logger.info('Done extracting "' + member_path + '"')
    
    logger.info('Moving extracted file to "' + output_filepath + '"')
    
    move(str(Path(output_filepath) / member_path), str(Path(output_filepath) / Path(member_path).name))
    os.rmdir(str(Path(output_filepath) / "home/sdf"))
    os.rmdir(str(Path(output_filepath) / "home"))
    
    logger.info('Moved extracted file')
    
    
if __name__ == '__main__':
    # Setup logging.
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Setup project dir reference.
    project_dir = Path(__file__).resolve().parents[2]

    main()

# data/__init__.py
#
# Loads in useful utilities for handling features.
import pandas as pd
import shutil
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src import DIRS, MISSING

# Get project directory.
DATA_DIRS = {
    'raw': DIRS.get("data.raw", None),
    'interim': DIRS.get("data.interim", None),
    'processed': DIRS.get("data.processed", None),
}

# Get basefile names.
DATA_FILENAMES = {
    'raw.zip': "walmart-product-data-2019.zip",
    'raw.csv': "marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv",
    'raw.gitkeep': ".gitkeep",
    'interim.basename': "ecommerce_data",
}

# Zip file structure.
ARCHIVE_PATH = DIRS.get("archive", None) # "home/sdf/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv"

def display_paths():
    """Useful debugger for seeing if script is loaded.
    """
    print("Project directory: {}".format(DIRS.get(".", MISSING)))
    print("Raw data directory: {}".format(DATA_DIRS.get("raw")))
    print("Interim data directory: {}".format(DATA_DIRS.get("interim")))
    
    for name in DATA_FILENAMES:
        print("Dataset [{}]: '{}'".format(name, DATA_FILENAMES.get(name, MISSING)))

def get_filepath(filename, version, tag = "cleaned", ext = ".csv", dirPath = ""):
    """Get the dataset filepath.
    """    
    # Create the basename.
    basename = "{}-{}-{}{}".format(filename, tag, version, ext)    
    # Create and return the filepath.
    return Path(dirPath) / basename

def get_source_filepath(ext = ".zip"):
    """Get the source filepath.
    """
    if ext == ".zip":
        basename = DATA_FILENAMES.get("raw.zip", MISSING)
    elif ext == ".gitkeep":
        basename = DATA_FILENAMES.get("raw.gitkeep", MISSING)
    elif ext == ".csv":
        basename = DATA_FILENAMES.get("raw.csv", MISSING)
    else:
        basename = MISSING
    return Path(DATA_DIRS.get('raw')) / basename

def get_interim_filepath(version, tag = "cleaned", ext = ".csv"):
    """Get the interim dataset filepath.
    """
    return get_filepath(DATA_FILENAMES.get('interim.basename'), version, tag = tag, ext = ext, dirPath = DATA_DIRS.get('interim'))

def save_dataset(df, filename, version, tag = "cleaned", dirPath = ""):
    """Save the dataset artifact.
    """
    # Get the filepath.
    filepath = get_filepath(filename, version, tag = tag, ext = ".csv", dirPath = dirPath)
    print("Saving ({}) dataframe {} to {}.".format(tag, df.shape, filepath))

    # Save the dataframe.
    df.to_csv(filepath)
    print("File saved.")

def save_data(logger, df_clean, output_filepath):
    # Target directory
    logger.info(f'Saving file to "{output_filepath}".')

    # Save the file.
    df_clean.to_csv(str(output_filepath))
    logger.info("File saved.")
    
def save_interim(df, version):
    """Save the cleaned artifact.
    """
    save_dataset(df, DATA_FILENAMES.get('interim.basename'), version, tag = "cleaned", dirPath = DATA_DIRS.get('interim'))
    
def load_envvars(logger):
    """ Load the environment variables for Kaggle authentication.
    """    
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    logger.info("Loading envvars...")
    load_dotenv(find_dotenv())
    logger.info("Done loading envvars.")
    
    
def move(logger, input_filepath, output_filepath):
    """Move dataset file to the output directory location.

    :param logger: Logger.
    :param input_filepath: Input filepath.
    :param output_filepath: Output directory path.
    """
    # Get the file.
    logger.info(f"Moving dataset from '{input_filepath}' into '{output_filepath}'...")

    # Check if source file exists.
    if not Path(input_filepath).is_file():
        logger.error(f"Cannot find file at '{input_filepath}'.")
        return False
    else:
        logger.info(f"Found file at '{input_filepath}'.")

    logger.info(f"Moving dataset to output location {output_filepath}...")

    # Move the dataset, overwriting if it exists.
    shutil.move(str(input_filepath), str(output_filepath))
    logger.info("Moved dataset successfully.")
    return True

def read_data(logger, input_filepath):
    """Read data from the input filepath location.
    
    @param input_filepath: Input filepath.
    """
    logger.info(f"Reading data from {input_filepath}")
    return pd.read_csv(input_filepath)
    
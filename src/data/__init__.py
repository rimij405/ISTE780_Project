# data/__init__.py
#
# Loads in useful utilities for handling features.
from pathlib import Path

# Equivalent to "./../../" which is the root directory.
PROJECT_DIR = Path(".").resolve().parents[0]
    
# Get project directory.
DATA_DIRS = {
    'raw': PROJECT_DIR / "data/raw",
    'interim': PROJECT_DIR / "data/interim",
    'processed': PROJECT_DIR / "data/processed"
}

# Get basefile names.
DATASETS = {
    'source.zip': "walmart-product-data-2019.zip",
    'source.csv': "marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv",
    'interim': "ecommerce_data"
}

def display_paths():
    """Useful debugger for seeing if script is loaded.
    """
    print("Project directory: {}".format(PROJECT_DIR))
    print("Raw data directory: {}".format(DATA_DIRS['raw']))
    print("Interim data directory: {}".format(DATA_DIRS['interim']))
    
    for name in DATASETS:
        print("Dataset [{}]: '{}'".format(name, DATASETS[name]))

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
        basename = DATASETS['source.zip']
    else:
        basename = DATASETS['source.csv']
    return Path(DATA_DIRS['raw']) / basename

def get_interim_filepath(version, tag = "cleaned", ext = ".csv"):
    """Get the interim dataset filepath.
    """
    return get_filepath(DATASETS['interim'], version, tag = tag, ext = ext, dirPath = DATA_DIRS['interim'])

def save_dataset(df, filename, version, tag = "cleaned", dirPath = ""):
    """Save the dataset artifact.
    """
    # Get the filepath.
    filepath = get_filepath(filename, version, tag = tag, ext = ".csv", dirPath = dirPath)
    print("Saving ({}) dataframe {} to {}.".format(tag, df.shape, filepath))

    # Save the dataframe.
    df.to_csv(filepath)
    print("File saved.")
        
def save_interim(df, version):
    """Save the cleaned artifact.
    """
    save_dataset(df, DATASETS['interim'], version, tag = "cleaned", dirPath = DATA_DIRS['interim'])
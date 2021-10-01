# dodo.py
#
# Tasks in this file are executed by the doit cli.

DOIT_CONFIG = { 'action_string_formatting': 'both' }

def task_download_dataset():
    """
    Download the dataset from Kaggle.
    """
    return {
        'targets': [ 'data/raw/walmart-product-data-2019.zip' ],
        'actions': [ 'python src/data/download_dataset.py {targets}' ],
        'clean': True
    }

def task_unpack_dataset():
    """
    Unpack the raw dataset (.zip) as the (.csv) file.
    """
    return {
        'file_dep': [ 'data/raw/walmart-product-data-2019.zip' ],
        'targets': [ 'data/raw/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv' ],
        'actions': [ 'python src/data/make_dataset.py {dependencies} data/raw' ],
        'clean': True
    }
    
def task_clean_dataset():
    """
    Clean the raw dataset (.csv) and place in the interim folder.
    """
    return {
        'file_dep': [ 'data/raw/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv' ],
        'targets': [ 'data/interim/ecommerce_data-cleaned-0.1.csv' ],
        'actions': [ 'python src/data/clean_dataset.py {dependencies} {targets}' ],
        'clean': True
    }
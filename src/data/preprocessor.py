# -*- coding: utf-8 -*-
# cleaner.py
# -----------
# Perform data cleaning on the raw dataset.
import click
import logging
import pandas as pd
from pathlib import Path
from . import load_envvars, read_data, save_data, get_interim_filepath, ARCHIVE_PATH
from .preprocessing import filter

@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
def main(input_filepath):
    """Clean the dataset and provide intermediate outputs."""
    return clean(input_filepath)


def clean(input_filepath):
    """Clean the dataset and provide intermediate outputs.

    @param input_filepath: Raw dataset to be manipulated.
    """
    # Filter the dataframe.
    df = filter(input_filepath, get_interim_filepath(0.1))
    
    return df

def get_cached(logger, cache_filepath):
    # Does cache exist?
    if cache_filepath.is_file():
        logger.warning("DONE. Cached file found for this stage of cleaning.")
        return read_data(logger, cache_filepath)
    else:
        return None

def filter(input_filepath, output_filepath):
    """Perform filtering on the input pd.DataFrame.

    @param input_filepath: Input filepath.
    @param output_filepath: (Optional) If provided, exports an interim file to this location.
    """
    logger = logging.getLogger(__name__)
    
    # Does cache exist?
    output_filepath = Path(output_filepath)
    cached_df = get_cached(logger, output_filepath)
    if cached_df is not None:
        return cached_df

    if not output_filepath.parents[0].is_dir():
        output_filepath.parents[0].mkdir(parents=True, exist_ok=True)

    input_filepath = Path(input_filepath)
    input_df = read_data(logger, input_filepath)
    if not isinstance(input_df, pd.DataFrame):
        # If no provided filepath and no cache, fail.
        logger.error("FAILED. Cannot filter null dataframe.")
        raise ValueError("Missing dataframe.")

    # Filtering of the data frame.
    df_clean = filter.remove_features(input_df)
    df_clean = filter.remove_bad_prices(df_clean)
    
    # Save the intermediate cleaned dataframe.
    save_data(logger, df_clean, output_filepath)
    logger.warning(f"DONE. Cleaned file has been cached at '{output_filepath}'")
    return df_clean

def clean2(input_filepath, output_filepath):
    pass

# Executes when 'main' is set.
if __name__ == "__main__":
    # Prepare the logging format and level.
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Execute the main function.
    main()

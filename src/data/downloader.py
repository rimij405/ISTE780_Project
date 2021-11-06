# -*- coding: utf-8 -*-
# downloader.py
# -------------
# Downloads the raw dataset from the Kaggle API
# and moves the resulting zipfile into the output filepath.
import click
import logging
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
from . import load_envvars, move


@click.command()
@click.argument("output_dir", type=click.Path())
@click.argument("output_filename", type=click.Path())
def main(output_dir, output_filename):
    """Download raw dataset using the Kaggle API."""
    return download(output_dir, output_filename)


def download(output_dir, output_filename):
    """Download raw dataset using the Kaggle API.

    @param output_dir: Absolute or relative Path() pointing to output directory.
    @param output_filename: Relative Path() representing the output filename.
    """
    # Get logger.
    logger = logging.getLogger(__name__)

    # Form the output filepath.
    output_filepath = Path.cwd() / output_dir / output_filename
    logger.info(f"Downloading raw dataset to '{output_filepath}'...")

    # Create if output directory if it does not exist.
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Check if output filepath exists.
    if Path(output_filepath).is_file():
        logger.warning(
            f"DONE. Dataset '{output_filename}' already exists at specified location."
        )
        return True

    # Load envvars for Kaggle authentication.
    load_envvars(logger)

    # Authenticate
    api = authenticate(logger)

    # Download the kaggle dataset.
    # https://technowhisp.com/kaggle-api-python-documentation/
    logger.info("Downloading dataset...")
    api.dataset_download_files(
        "promptcloud/walmart-product-data-2019", quiet=False, unzip=False
    )
    # kaggle datasets download -d promptcloud/walmart-product-data-2019

    # Move to the next location.
    return move(logger, Path("walmart-product-data-2019.zip"), Path(output_filepath))


def authenticate(logger):
    """Authenticate to the KaggleAPI."""
    # Note: User must have kaggle.json API authentication
    # token saved to the correct location.

    # Authenticate.
    logger.info("Authenticating to the Kaggle API...")
    api = KaggleApi()
    api.authenticate()
    logger.info("Done authenticating to the Kaggle API.")
    return api


# Executes when 'main' is set.
if __name__ == "__main__":
    # Prepare the logging format and level.
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Execute the main function.
    main()

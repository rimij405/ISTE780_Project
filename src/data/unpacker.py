# -*- coding: utf-8 -*-
# unpacker.py
# -----------
# Extract data from the raw dataset's zip file.
import click
import logging
from os import rmdir
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
from . import load_envvars, move, ARCHIVE_PATH


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
@click.argument("output_filename", type=click.Path())
def main(input_filepath, output_dir, output_filename):
    """Extract zipped raw dataset into an unpacked format."""
    return extract(input_filepath, output_dir, output_filename)


def extract(input_filepath, output_dir, output_filename):
    """Extract zipped raw dataset into an unpacked format.

    @param input_filepath: Path() representing the input file.
    @param output_dir: Path() representing the output file directory.
    @param output_filename: Relative Path() representing the output filename.
    """
    # Get the logger.
    logger = logging.getLogger(__name__)

    # Load the envvars.
    load_envvars(logger)

    # Form the output filepath.
    output_filepath = Path.cwd() / output_dir / output_filename
    logger.info(f"Exporting zipped dataset contents to '{output_filepath}'...")

    # Create if output directory if it does not exist.
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Check if output filepath exists.
    if Path(output_filepath).is_file():
        logger.warning(
            f"DONE. Dataset {output_filename} already exists unzipped at specified location."
        )
        return True

    # Check if input filepath exists.
    if not Path(input_filepath).is_file():
        logger.error(
            f"FAILED. Cannot unzip dataset. No dataset present at '{input_filepath}'."
        )
        return False

    # Extract the dataset from the archive file.
    input_dir = Path(input_filepath).resolve().parents[0]
    extract_path = input_dir.joinpath(ARCHIVE_PATH)
    extract_dir = extract_path.parents[0]
    logger.info(
        f"Extracting zip://{ARCHIVE_PATH} from '{input_filepath}' to '{extract_path}'..."
    )
    # Reference: https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/
    with ZipFile(input_filepath, "r") as zf:
        zf.extract(str(PurePosixPath(ARCHIVE_PATH)), input_dir)
        logger.info(f"Extraction of {ARCHIVE_PATH} successful.")

    # Move file into appropriate final location.
    logger.info(f"Moving extracted files to '{output_filepath}'...")
    move(logger, Path(extract_path), Path(output_filepath))
    rmdir(str(extract_dir))
    rmdir(str(extract_dir.parents[0]))

    # Notify user extraction completed successfully.
    logger.info("DONE. Extraction completed successfully.")
    return True


# Executes when 'main' is set.
if __name__ == "__main__":
    # Prepare the logging format and level.
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Execute the main function.
    main()

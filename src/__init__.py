# src/__init__.py
# ---------------
# Load in useful constants.
from pathlib import Path

MISSING = "<MISSING>"

DIRS = {
    '.': Path.cwd(),
    'data.raw': Path.cwd().joinpath("data", "raw"),
    'data.interim': Path.cwd().joinpath("data", "interim"),
    'data.processed': Path.cwd().joinpath("data", "processed"),
    'archive': Path("home/sdf/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv"),
}


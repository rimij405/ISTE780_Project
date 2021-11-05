# data.py
# --------
# Tasks associated with setting up the dataset.
from pathlib import Path
from doit.tools import create_folder, run_once
from doit.action import CmdAction, PythonAction
from src.data import download_dataset, make_dataset
import sys

DATA_DIR = Path.cwd() / "data/"

DATA = {
    ".gitkeep": "data/.gitkeep",
    "raw": {
        "zip": "data/raw/walmart-product-data-2019.zip",
        "csv": "data/raw/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv",
    },
    "interim": [
        "data/interim/ecommerce_data-cleaned-0.1.csv",
    ],
}


def task_create_data_dir():
    """
    Create the data directory.
    """
    # uptodate
    def dir_exists():
        """
        Check if gitkeep and data directory already exists.
        """
        return DATA_DIR.exists() and DATA_DIR.joinpath(".gitkeep").exists()

    # action
    def make_targets(targets):
        """
        Create empty files at target locations.
        """
        for target in targets:
            filepath = Path(target)
            filepath.touch(exist_ok=True)

    return {
        "uptodate": [dir_exists],
        "actions": [(create_folder, [DATA_DIR]), make_targets],
        "targets": [DATA[".gitkeep"]],
    }


def task_download_data():
    """
    Download the dataset from Kaggle.
    """

    def download(targets):
        """
        Download data associated with all specified targets.
        """
        return sys.executable + " src/data/download_dataset.py {targets}"

    return {
        "uptodate": [run_once],
        "task_dep": ["create_data_dir", "create_env"],
        "actions": [(create_folder, [DATA_DIR / "raw"]), CmdAction(download)],
        "targets": [DATA["raw"]["zip"]],
        "clean": True,
    }


def task_unpack_data():
    """
    Unpack the raw dataset (.zip) as the (.csv) file.
    """

    def unpack(dependencies):
        """
        Unpack the dataset.
        """
        return sys.executable + " src/data/make_dataset.py {dependencies} data/raw"

    return {
        "file_dep": [DATA["raw"]["zip"]],
        "task_dep": ["download_data"],
        "actions": [CmdAction(unpack)],
        "targets": [DATA["raw"]["csv"]],
        "clean": True,
    }


def task_clean_data():
    """
    Clean the raw dataset (.csv) and place in the interim folder.
    """

    def clean(dependencies, targets):
        """
        Clean the existing dataset files.
        """
        return sys.executable + " src/data/clean_dataset.py {dependencies} {targets}"

    return {
        "file_dep": [DATA["raw"]["csv"]],
        "task_dep": ["unpack_data"],
        "actions": [(create_folder, [DATA_DIR / "interim"]), CmdAction(clean)],
        "targets": [*DATA["interim"]],
        "clean": True,
    }

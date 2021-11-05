# data.py
# --------
# Tasks associated with setting up the dataset.
from pathlib import Path
from doit.tools import create_folder, run_once
from doit.action import CmdAction, PythonAction
from src.data.download_dataset import download
import sys

DATA_DIR = Path.cwd() / "data/"


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
        "targets": ["data/.gitkeep"],
    }


def task_download_dataset():
    """
    Download the dataset from Kaggle.
    """

    def download_data(targets):
        """
        Download data associated with all specified targets.
        """
        download(targets[0])

    return {
        "uptodate": [run_once],
        "task_dep": ["create_data_dir", "create_env"],
        "actions": [(create_folder, [DATA_DIR / "raw"]), download_data],
        "targets": ["data/raw/walmart-product-data-2019.zip"],
        "clean": True,
    }

# data.py
# --------
# Tasks associated with setting up the dataset.
from pathlib import Path
from doit.tools import create_folder, run_once
from doit.action import CmdAction, PythonAction
from src.data import (
    DATA_DIRS,
    DATA_FILENAMES,
    get_source_filepath,
    get_interim_filepath,
)
from src.data.downloader import download
from src.data.unpacker import extract
from src.data.preprocessor import filter


def task_create_data_dir():
    """
    Create the data directory.
    """
    # uptodate
    def dir_exists():
        """
        Check if gitkeep and data directory already exists.
        """
        return (
            DATA_DIRS.get("raw").is_dir()
            and get_source_filepath(ext=".gitkeep").is_file()
        )

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
        "actions": [(create_folder, [DATA_DIRS.get("raw")]), make_targets],
        "targets": [get_source_filepath(ext=".gitkeep")],
    }


def task_download_data():
    """
    Download the dataset from Kaggle.
    """

    def download_targets(targets):
        """
        Download data associated with all specified targets.
        """
        target = targets[0]
        print(target)
        return download(DATA_DIRS.get("raw"), Path(target).name)
        # return sys.executable + " src/data/download_dataset.py data/raw {Path(target).name}"

    return {
        "uptodate": [run_once],
        "task_dep": ["create_data_dir", "create_env"],
        "actions": [(create_folder, [DATA_DIRS.get("raw")]), download_targets],
        "targets": [get_source_filepath(ext=".zip")],
        "clean": True,
    }


def task_unpack_data():
    """
    Unpack the raw dataset (.zip) as the (.csv) file.
    """

    def extract_deps(dependencies, targets):
        """
        Unpack the dataset.
        """
        dep = Path(dependencies[0])
        target = Path(targets[0])
        target_dir = target.parents[0]
        return extract(dep, target_dir, target)
        # return sys.executable + " -m src.data.unpacker {dependencies} data/raw "

    return {
        "file_dep": [get_source_filepath(ext=".zip")],
        "task_dep": ["download_data"],
        "actions": [extract_deps],
        "targets": [get_source_filepath(ext=".csv")],
        "clean": True,
    }


def task_clean_data():
    """
    Clean the raw dataset (.csv) and place in the interim folder.
    """

    def filter_data(dependencies, targets):
        """
        Clean the existing dataset files.
        """
        dep = dependencies[0]
        target = targets[0]
        df = filter(dep, target)
        return df.shape[0] > 0
        # return sys.executable + " src/data/clean_dataset.py {dependencies} {targets}"

    # def clean2_data(dependencies, targets):
        # """
        # Next step.
        # """
        # dep = targets[0]
        # target = targets[1]
        # return clean2(dep, target)

    return {
        "file_dep": [get_source_filepath(ext=".csv")],
        "task_dep": ["unpack_data"],
        "actions": [(create_folder, [DATA_DIRS.get("interim")]), filter_data],
        "targets": [get_interim_filepath(0.1)],
        "clean": True,
    }

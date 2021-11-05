# data.py
# --------
# Tasks associated with setting up the dataset.
from pathlib import Path
from doit.tools import create_folder
from doit.action import CmdAction, PythonAction
import sys

DATA_DIR = Path.cwd() / "data/"


def task_create_data_dir():
    """
    Create the data directory.
    """

    def make_targets(targets):
        """
        Create empty files at target locations.
        """
        for target in targets:
            filepath = Path(target)
            filepath.touch(exist_ok=True)

    return {
        "actions": [(create_folder, [DATA_DIR]), make_targets],
        "targets": ["./data/.gitkeep"],
    }

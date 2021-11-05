# dodo.py
# Reference: https://pydoit.org/
# -------
# Tasks in this file are executed by the doit cli tool.

from doit import exceptions
from doit.tools import run_once
from doit.action import CmdAction, PythonAction
from pathlib import Path
import os
import sys

from tasks.conda import task_create_env
from tasks.data import *

# Ensures that the called Python is the same interpreter
# used by the one that called the `doit` tasks.
EXECUTABLE = sys.executable

# Configure the task runner's settings.
DOIT_CONFIG = {"verbosity": 2, "action_string_formatting": "both"}

# Get reference to the working directory.
CWD = Path.cwd()




def _task_clean_dataset():
    """
    Clean the raw dataset (.csv) and place in the interim folder.
    """
    return {
        "file_dep": [
            "data/raw/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv"
        ],
        "targets": ["data/interim/ecommerce_data-cleaned-0.1.csv"],
        "actions": [EXECUTABLE + " src/data/clean_dataset.py {dependencies} {targets}"],
        "clean": True,
    }


if __name__ == "__main__":
    import doit

    doit.run(globals())

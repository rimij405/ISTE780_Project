# dodo.py
# Reference: https://pydoit.org/
# -------
# Tasks in this file are executed by the doit cli tool.
from pathlib import Path

# See the tasks/ folder for more information.
from tasks.conda import *
from tasks.data import *

# Configure the task runner's settings.
DOIT_CONFIG = {
    "verbosity": 2,
    "action_string_formatting": "both",
}

if __name__ == "__main__":
    import doit

    doit.run(globals())

# conda.py
# --------
# Tasks associated with setting up the conda environment.
from pathlib import Path
from doit.exceptions import TaskFailed
from doit.action import CmdAction, PythonAction
import sys


def env_active():
    """
    Determine if the local conda environment
    python is currently being used.
    """
    env_python = Path(".condaenv/python.exe")
    exe_python = Path(sys.executable)
    is_active = env_python.resolve() == exe_python.resolve()
    print(f"Is the conda environment python the same as the current one? [{is_active}]")
    return is_active


def task_create_env():
    """
    Create new conda environment using 'environment.yaml'.
    """

    # uptodate
    def env_exists():
        """
        Determine if the local conda environment '.condaenv'
        exists in the current working directory.
        """
        # Get the path to the conda environment.
        env_path = Path.cwd() / ".condaenv"

        # Ensure folder directory exists and is a path.
        env_found = env_path.exists() and env_path.is_dir()

        # Pass result.
        return env_found

    # action
    def create_env():
        """
        Create local prefixed conda environment using the command line.
        """
        if not env_active():
            return TaskFailed("Cannot complete task without using correct conda environment.")
        if env_exists():
            return "echo 'DONE (Conda environment already exists)'"
        return "conda env create --prefix=.condaenv -f=environment.yaml"

    # task metadata
    return {
        "uptodate": [env_exists],
        "file_dep": ["environment.yaml"],
        "actions": [CmdAction(create_env)],
        "targets": [".condaenv/python.exe"],
    }

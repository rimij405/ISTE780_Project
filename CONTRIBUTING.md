# Contributing Guide

This is a contributing guide communicating how a contributor can contribute to the development of this project. At this time, only the project maintainers can contribute to this repository.

## How to get started

To use this project, begin by forking this repository. Once this process is complete, clone the project to your local development environment.

## Installation

Once you've cloned the project to your local working environment, you'll need to install the project dependencies.

There are several options at this stage:

If you have `conda`, create a new environment and install the dependencies using the `environment.yaml` file:

```bash
conda env create -f environment.yaml
```

If you have `pip`, install your dependencies using the `setuptools`, `wheel`, and the `requirements.txt` file:

```bash
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -r requirements.txt
```

Alternatively, if you are familiar with `Makefile`s, you could attempt to use the `make` commands within [Makefile](Makefile) in order to automate the process.

## Setting up the Environment

You'll want to add a `.env` file to your project's root directory if you want to use the Kaggle API to pull in live data.

```python
# PROJECT_ROOT/.env

# Environment variables go here, can be read by `python-dotenv` package:
#
#   `src/script.py`
#   ----------------------------------------------------------------
#    import dotenv
#
#    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
#    dotenv_path = os.path.join(project_dir, '.env')
#    dotenv.load_dotenv(dotenv_path)
#   ----------------------------------------------------------------
#
# DO NOT ADD THIS FILE TO VERSION CONTROL!

# Kaggle API key-value pairs. Uncomment as needed.
# Reference: https://stackoverflow.com/questions/49386920/download-kaggle-dataset-by-using-python
KAGGLE_USERNAME = "xxxx"
KAGGLE_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Consider copying the above code block into your new file and go from there.

## Retrieving the Data

You may need to retrieve the data for your local environment. As per Kaggle rules, we do not rehost the data, but we do provide means for accessing it.  Please review Kaggle's [terms of service](https://www.kaggle.com/terms) before working with their data.

You can access the dataset by visiting the [Walmart Product Data 2019](https://www.kaggle.com/promptcloud/walmart-product-data-2019) Kaggle dataset by PromptCloud.

## Development

### Pick the Right Branch

To keep track of development, please consider using the following branches to correspond to your changes:

- `main`: This branch is the closest to a `production` branch. Just before each checkpoint, we can merge our changes into `main` to prepare for submission.
- `development`: This branch should contain in-progress and under-development features. This can include model training, fitting, and other machine learning tasks.
- `experimental`: This branch should contain experimental work related to analysing and preprocessing the data. If there's a new technique you would like to try that modifies the data preparation pipeline, it should go here.

Separation of concerns between these branches allows individual analyses to take place. Once you have completed your local changes, please make a pull request against the appropriate branch in the upstream repository.

From time to time, the `experimental` branch will be merged into the `development` branch and rebased. Likewise, the `development` branch will be merged into the `main` branch, prior to checkpoints, and rebased.

## Pull Requests

So you've completed your notebook analysis or refactored a script that completes an important task. When you're ready to share your changes with the rest of the team, it's time to fill out a pull request.

When you make a PR, make a pull against the appropriate "WIP" branch: either `development` or `experimental`. Once a PR request has been made, please notify the repository maintainers.

## Attribution

This guide is based off of the [contributing template](https://github.com/nayafia/contributing-template) provided by [@nayafia](https://github.com/nayafia). The original template is available under the Creative Commons CC0 1.0 License.

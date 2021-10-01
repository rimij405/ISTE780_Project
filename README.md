# Walmart Product Data: Price Classifier

## Overview

This project covers the extraction and evaluation of Walmart product data features for classification of list price ranges. This project has been attempted as part of the [ISTE 780: Data-Driven Knowledge Discovery](https://www.rit.edu/online/study/information-sciences-and-technologies-ms#:~:text=Credits%203-,ISTE-780,-Data%20Driven%20Knowledge) course at the [Rochester Institute of Technology](https://rit.edu/).

## Getting Started

1. Fork this repository.
2. Clone the repository to your local environment.
3. Install the dependencies. There are 3 separate options:
   1. Use the `requirements.txt` file if you use `pip`.
   2. Use the `environment.yaml` file if you use `conda` or `mamba`.
   3. Use the `Makefile` if you are familiar with how to operate it.

You can read more about how to get started by reviewing the [contributing guide](CONTRIBUTING.md).

## Project Organization

    ├── LICENSE
    ├── dodo.py            <- Contains build tasks. Replaces the typical MAKEFILE with a Python automation script.
    ├── CONTRIBUTING.md    <- Contributing guide for developers wishing to contribute.
    ├── README.md          <- The top-level README for developers using this project.
    ├── .env               <- File with envvars accessible by `python-dotenv`. Not added to version control.
    |
    ├── data/              <- Data folder is not included in version control.
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs/               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models/             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks/          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's identifier (eg. initials or GitHub username), and a short `-` delimited description, e.g.
    │                         `1.0-rimij405-initial-data-exploration`.
    │
    ├── references/         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports/            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures/        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src/               <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data/          <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features/       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models/         <- Scripts to train models and then use trained models to make predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization/  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── test/               <- Test scripts to be executed by pytest

## Attributions

### Citations

PromptCloud (2019). [Walmart Product Data 2019](https://www.kaggle.com/promptcloud/walmart-product-data-2019).

The crawled data was bundled into datasets that can be used by the general public for various purposes. It was released under the [CC0: Public Domain license](https://creativecommons.org/publicdomain/zero/1.0/).

### Project Template

Project based on the [cookiecutter data science](https://drivendata.github.io/cookiecutter-data-science/)  project template. Read more about the [cookiecutter tool here](https://cookiecutter.readthedocs.io/en/latest/README.html).

[#cookiecutterdatascience](https://github.com/topics/cookiecutter-data-science)

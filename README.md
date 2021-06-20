# Instructions on how to run app
## Table of contents
1. Set up environment
2. Run application

## 1. Set up virtual environment for project

### Install and upgrade pip

`python3 -m pip install --user --upgrade pip`

### Install the virtualenv package

`python3 -m pip install --user virtualenv`

### Create the virtual environment

`python3 -m venv env`

### Activate the virtual environment

`source env/bin/activate`

### Install requirements

`pip install -r requirements.txt`

## 2. Running the main program
1. Ensure the current working directory is ``levenshtein/``
2. Run ``python3 src/main.py``
3. Find a csv of unique dog names with Levenshtein Distance = 1 in ``output/names.csv``
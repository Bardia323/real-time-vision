#!/bin/bash

# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# install necessary packages
python -m pip install -r requirements.txt

# setup config
python server/config.py
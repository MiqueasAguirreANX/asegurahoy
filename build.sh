#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python3 -m pip install --upgrade pip setuptools wheel
python3 manage.py collectstatic --no-input
python3 manage.py migrate
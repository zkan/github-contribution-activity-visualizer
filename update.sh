#!/bin/bash

pipenv run python program.py > index.html
git add index.html
git commit -m "Update contributions on $(date)"
git push origin master

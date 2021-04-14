#!/bin/bash
echo Activating virtual env
start_dir=$(PWD)
export PIPENV_PIPFILE=~/.work-env/my-work-environment/Pipfile
pipenv shell cd $start_dir

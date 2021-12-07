#!/bin/bash
echo "Activating virtual env for databaker-docker branch: ${WORK_ENV_BRANCH}"
start_dir=$(PWD)
export PIPENV_PIPFILE=~/.work-env/my-work-environment/Pipfile
pipenv run python3 ~/.work-env/scripts/check_dependencies.py
pipenv shell cd $start_dir

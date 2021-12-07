# Basic info for user
echo Activating virtual env
echo --------------------------
echo BRANCH IS: ${WORK_ENV_BRANCH}
echo --------------------------

# Delete any lingering venv from last time
mkdir -p ~/.work-env/my-work-environment
cd ~/.work-env/my-work-environment
pipenv --rm
cd ~/.work-env

# Update work-env
#git stash
#git pull

# Get latest Pipfile and Pipfile.lock
curl -L https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/${WORK_ENV_BRANCH}/Pipfile -o ~/.work-env/my-work-environment/Pipfile
curl -L https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/${WORK_ENV_BRANCH}/Pipfile.lock -o ~/.work-env/my-work-environment/Pipfile.lock

# Build the venv
export PIPENV_PIPFILE=~/.work-env/my-work-environment/Pipfile
echo Adding missing wheel where needed
pipenv run pip install wheel
echo Installing dependencies from databaker-docker
pipenv sync --dev
echo Installing any additional dependencies
pipenv run python3 ~/.work-env/scripts/extend_environment.py
pipenv install -r ~/.work-env/additional-requirements.txt --skip-lock

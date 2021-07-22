echo Activating virtual env
start_dir=$(PWD)
mkdir -p ~/.work-env/my-work-environment
cd ~/.work-env/my-work-environment
pipenv --rm
cd ~/.work-env
git stash
git pull
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile -o ~/.work-env/my-work-environment/Pipfile
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock -o ~/.work-env/my-work-environment/Pipfile.lock
export PIPENV_PIPFILE=~/.work-env/my-work-environment/Pipfile
export PIP_NO_CACHE_DIR=true
pipwnv install "wheel"
pipenv install --skip-lock
pipenv run python3 ~/.work-env/scripts/extend_environment.py
pipenv install --skip-lock -r ~/.work-env/additional-requirements.txt

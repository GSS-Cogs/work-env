echo Activating virtual env
start_dir=$(PWD)
mkdir -p ~/.work-env/my-work-environment
cd ~/.work-env/my-work-environment
git pull
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile -o ~/.work-env/my-work-environment/Pipfile
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock -o ~/.work-env/my-work-environment/Pipfile.lock
pipenv install
pipenv shell cd $start_dir

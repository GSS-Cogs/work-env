echo Activating virtual env
start_dir=$(PWD)
mkdir -p ~/.work-env/my-work-environment
cd ~/.work-env
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile -o ~/my-work-environment/Pipfile
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock -o ~/my-work-environment/Pipfile.lock
python3 $PWD/attach-scripts.py
pipenv install
pipenv shell cd $start_dir

echo Activating virtual env
start_dir=$(PWD)
mkdir -p ~/.work-env/my-work-environment
cd ~/.work-env/my-work-environment
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile -o ~/.work-env/my-work-environment/Pipfile
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock -o ~/.work-env/my-work-environment/Pipfile.lock
python3 attach-scripts.py
export PIPENV_PIPFILE=~/.work-env/my-work-environment/Pipfile
pipenv install
curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/convenience/scripts.sh?token=ADQULFIQA3LWXOCNGYERBULAP4KSI -o scripts.sh
pipenv shell cd $start_dir

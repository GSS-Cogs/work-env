# Update with any local only dependencies
curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/additional-requirements.txt?token=ADQULFJYSU5LMKKZZBYVQ4LAP4KQE -o requirements.txt
pipenv install -r requirements.txt

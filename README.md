# installation
```zsh
# clone repo
python -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install

events migrate
events createsuperuser
events runserver
```

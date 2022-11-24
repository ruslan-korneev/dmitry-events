# installation
```zsh
# clone repo
python -m venv .venv
. .venv/bin/activate
poetry install

python src/manage.py migrate
python src/manage.py createsuperuser
python src/manage.py runserver
```


# Proposals
- i would make ticket with some owner unique for one event
- i would make a winner in event model -> ticket_id

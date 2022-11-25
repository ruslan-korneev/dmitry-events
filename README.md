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

# using docker-compose
```zsh
cat env_sample > .env  # change variables to required for you
scripts/export-schema.sh

docker-compose up -d
# for new docker: `docker compose up -d`
```

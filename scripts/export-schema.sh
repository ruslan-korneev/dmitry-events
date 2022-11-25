#!/bin/zsh

. .venv/bin/activate
export DJANGO_SETTINGS_MODULE=src.events_project.spectacular_settings

rm -f schema.yml schema.json

events spectacular --file schema.yml
events spectacular --file schema.json --format openapi-json


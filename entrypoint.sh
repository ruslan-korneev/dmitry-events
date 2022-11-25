#!/bin/bash

events collectstatic --noinput
events migrate
"$@"

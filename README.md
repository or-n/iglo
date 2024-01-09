# IGLO

You need Python 3.10 to run this project.

## Dev workflow and useful commands:

```
# Virtual env

virtualenv /tmp/iglo
source /tmp/iglo/bin/activate
pip install poetry
poetry install

# Setup

export IGLO_DB_PORT=15432  # envvar needed for manage and other commands
export CELERY_TASK_ALWAYS_EAGER=True
alias manage="poetry run python3 iglo/manage.py"

docker ps -a  # Optionally: docker stop iglo-db; docker rm iglo-db
docker run -e POSTGRES_PASSWORD=postgres --name iglo-db -p ${IGLO_DB_PORT}:5432 -d postgres
manage migrate
manage load_seasons fixtures/seasons.json
manage createsuperuser

# Run server

manage runserver

# update translation file, then one can add translations

manage makemessages --all

# update accurating lib version

poetry cache clear PyPI --all  # sometimes
poetry add accurating@latest

# Running python with iglo and its libraries

# Celery dev run. Should not be needed because we run iglo with CELERY_TASK_ALWAYS_EAGER=True

export IGOR_MAX_STEPS=120
cd iglo
celery -A iglo worker -l INFO --concurrency 2 --max-tasks-per-child 50 --max-memory-per-child 200000

```

## Shell development

This will run python with iglo:
`manage shell`

And then inside you can run

```python
from importlib import reload
import league.igor as igor

igor.recalculate_igor()

# edit some code and reload to take new code into account:
reload(igor)
igor.recalculate_igor()

```

## Important links

- http://localhost:8000/admin/
- http://localhost:8000/league/admin

## Old instructions:

Local development (inside Python venv):

```
$ pip install poetry
$ poetry install
$ docker run --name iglo-db -p 5432:5432 -d postgres
$ python iglo/manage.py migrate
$ python iglo/manage.py runserver
```

Docker build & run:

```
$ ./deploy/build.sh
$ ./deploy/start.sh
```

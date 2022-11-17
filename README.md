# Santa Claus Service

[![CI](https://github.com/nekea/santa_claus/actions/workflows/backend.yml/badge.svg)](https://github.com/nekea/santa_claus/actions)



# Prerequisites

## Native way with virtualenv
- [Python3.10](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Docker way
- [Docker](https://docs.docker.com/engine/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)

## Local Development

## Native way with virtualenv

First create postgresql database:

```sql
create user santa_claus with createdb;
alter user santa_claus password 'santa_claus';
create database santa_claus owner santa_claus;
```
Now you can setup virtualenv and django:
```bash
virtualenv venv
source venv/bin/activate
pip install pip-tools
make bootstrap
```

## Docker way

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

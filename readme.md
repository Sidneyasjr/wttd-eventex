# Eventex

Projeto criado no curso Welcome to the Django

https://eventex-sidneyjunior.herokuapp.com/

## Usage:
Create project:
django-admin startproject --template https://github.com/Sidneyasjr/wttd-eventex/archive/main.zip --name=Procfile,.env myproject

Setup:
cd myproject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Deploy:
PRJ=myapp && \
git init && \
git add . && \
git commit -m 'Initial import' && \
heroku create $PRJ && \
heroku config:set DEBUG=True SECRET_KEY=`cat .env | grep SECRET_KEY | cut -d = -f 2` && \
heroku config:set DEBUG=True
git push heroku master

# fac-cedoc

###  startup
install virtualenv:

`sudo apt-get install virtualenv`

create virtualenv:

`virtualenv –p /usr/bin/python3 venv`

activate virtualenv (venv):

`source venv/bin/activate` or `. venv/bin/activate`

install django2.0:

`pip install django`

run server:

`python manage.py runserver` 

### utilities

connection with db:

`python manage.py migrate` 

create superuser:

`python manage.py createsuperuser`

static files (css and js):

`python manage.py collectstatic`

criar aplicação

`python manage.py startapp <name>`

#Instruções de Usuário

![Django](https://img.shields.io/badge/Django-v2.x-green.svg)


##  Começando
instalar o `virtualenv` para a criação de um ambiente virtual isolado: `sudo apt-get install virtualenv`

criar o ambiente: `virtualenv –p /usr/bin/python3 <name>` - recomenda-se utilzar o nome `venv`

ativar o ambiente para utiliza-lo: `source <name>/bin/activate` ou `. <name>/bin/activate`

o que deve estar instalado na sua virutalenv:

```
Django==2.0.6
Pillow==5.1.0
pkg-resources==0.0.0
pytz==2018.4
```

para instalar estes utilize o comando `pip install <nome>`

## Comandos úteis do Django

run server: `python manage.py runserver` 

make migrations with db: `python manage.py makemigrations`

connection with db: `python manage.py migrate` 

create superuser: `python manage.py createsuperuser`

static files (css and js): `python manage.py collectstatic`

criar aplicação: `python manage.py startapp <name>`
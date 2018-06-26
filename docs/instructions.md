# Instruções de Usuário

![Django](https://img.shields.io/badge/Django-v2.x-green.svg)


##  Começando

1. Instalar o `virtualenv` para a criação de um ambiente virtual isolado: `sudo apt-get install virtualenv`

2. Criar o ambiente: `virtualenv –p /usr/bin/python3 <name>` - recomenda-se utilzar o nome `venv`

3. Ativar o ambiente para utiliza-lo: `source <name>/bin/activate` ou `. <name>/bin/activate`

4. O que deve estar instalado na sua virutalenv:

```
Django==2.0.6
Pillow==5.1.0
pkg-resources==0.0.0
pytz==2018.4
```

5. Para instalar estes utilize o comando `pip install <nome>`

## Comandos úteis do Django

- Rodar o servidor: `python manage.py runserver` 

- Fazer migrações para o banco de dados: `python manage.py makemigrations`

- Conectar as migrações com o banco: `python manage.py migrate` 

- Criar super usuário: `python manage.py createsuperuser`

- Criar uma aplicação: `python manage.py startapp <name>`
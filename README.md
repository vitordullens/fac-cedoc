# FAC-CeDoc

## startup
install virtualenv:

```sudo apt-get install virtualenv```

create virtualenv:

```virtualenv –p /usr/bin/python3 venv```

activate virtualenv (venv):

```source venv/bin/activate```

install django2.0:

```pip install django```

rodar servidor:

```cd project/ && python3 manage.py runserver``` 

## utilities

criar conexao com db(por enquanto sqlite3):

```python3 manage.py migrate``` 

criar superusuario:

```python3 manage.py createsuperuser```

setar static files

```python3 manage.py collectstatic```

sincronizar banco de dados

```python3 manage.py syncdb```

criar aplicação

```python3 manage.py startapp <name>```

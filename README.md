# FAC-CeDoc

## startup
install virtualenv:

```sudo apt-get install virtualenv```

activate virtualenv (venv):

```source venv/bin/activate```

criar conexao com db(por enquanto sqlite3):

```python3 manage.py migrate``` 

criar superusuario:


```python3 manage.py createsuperuser```

rodar servidor:

```python3 manage.py runserver``` 
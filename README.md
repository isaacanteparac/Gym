# GYM

### Requerimmientos

- Python 3.11.3
- pip 22.3.1
- [DB Browser for SQLite - PortableApp](https://sqlitebrowser.org/dl/)
- [documentacion - jinja motor de plantillas](https://jinja.palletsprojects.com/en/3.1.x/)
- [documentation - orm models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [documentation - reacpy](https://reactive-python.github.io/reactpy-django/get-started/installation/)

### Ejecucion

- .\venv\Scripts\activate.bat (activar entorno virtual)
- **correr servidor local**
  - python manage.py runserver
- **ejecutar los test**
  - pytest
  - ![image](https://github.com/isaacanteparac/Gym/assets/69361351/b924f14f-544d-413e-9bb1-ff6a5ba372fb)


### Entorno Virtual

- > creacion
  - pip install virtualenv
  - virtualenv venv
- > activacion
  - .\venv\Scripts\activate.bat
- > instalacion modulos
  - pip install django
    - veririfacion de instalacion django-admin --version
  - pip install reactpy-django
  - pip install pytest-django
  - pip install channels[daphne]
  - pip install aiohttp

- > generar proyecto
  - django-admin startproject nombrePro .

### Generar Tablas

- add tablas en ./gym/models
- python manage.py makemigrations src
- python manage.py migrate
- agregar su respectivo __str__ en ./gym/models

### Generar Datos

- [datos randoms](https://www.mockaroo.com/)

### Administrar Base de Datos

- visualizar los modelos en ./admin.py
  - user: admin
  - password: admin
  - email: admin@admin.com
- [link](http://127.0.0.1:8000/admin)


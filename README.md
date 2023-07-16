# GYM JOJO's

### requerimmientos

- Python 3.11.3
- pip 22.3.1
- [download DB Browser for SQLite - PortableApp](https://sqlitebrowser.org/dl/)
- [documentacion - jinja motor de plantillas](https://jinja.palletsprojects.com/en/3.1.x/)
- [documentation - orm models](https://docs.djangoproject.com/en/4.2/topics/db/models/)

### entonrono virtual (no ejecutar )

- > creacion
  - pip install virtualenv
  - virtual venv
- > instalacion modulos
  - pip install django
    - veririfacion de instalacion django-admin --version
- > generar proyecto
  - django-admin startproject nombrePro .

### activacion entorno virtual (ejecutar)

- > activacion
  - .\venv\Scripts\activate.bat
- > generar tablas
  - add tablas en ./gym/models
  - python manage.py makemigrations gym
  - python manage.py migrate gym
  - agregar su respectivo __str__ en ./gym/models

### correr server ( ejecutar)

- python manage.py startapp gym
- *ejecutar* python manage.py runserver
- [localhost 8000](http://127.0.0.1:8000/)


### generar datos

- [generacon de datos randoms](https://www.mockaroo.com/)

### admin

- sirver para administrar la base de datos
- para poder visualizar las modelos se agregan en ./admin.py
- [link](http://127.0.0.1:8000/admin)
- user: admin
- password: admin
- email: admin@admin.com

## tutoriales

- [Django, Curso de Django para Principiantes](https://www.youtube.com/watch?v=T1intZyhXDU)
- [Django CRUD con Autenticacion](https://www.youtube.com/watch?v=e6PkGDH4wWA)

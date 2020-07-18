# Lab: 26 - Intro to Django

## App initial setup:

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
- `python manage.py runserver` - to run server

## <a name="env"></a> ENV variables:

SECRET_KEY=secret key for the app (typically 50-characters long string)  
DEBUG=should be set to True in development  
ALLOWED_HOSTS=localhost,127.0.0.1 (for testing)

## Routes:

`/` - welcome page;  
`/about/` - about page;

## Additional information:

## DB Schema:

No DB

## Dependency Documentation:

[Django (v. 3.0.8)](https://docs.djangoproject.com/en/3.0/)  
[Django-Environ (v. 0.4.5)](https://pypi.org/project/django-environ/)

### Dev Dependencies:

[pylint-django](https://pypi.org/project/pylint-django/)  
[autopep8](https://pypi.org/project/autopep8/)

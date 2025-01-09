# check if django is installed frm CLI:
 ```bash
 python3 -m django --version
 ```

# Django First Tuto App:
- source: https://docs.djangoproject.com/en/5.1/intro/tutorial01/

## Creating Django App instance:

- the importance of `__init__.py`: 
https://stackoverflow.com/questions/448271/what-is-init-py-for

- from the CLI u can create an instance of a django project with biolerplate code, to bootstrap a new project:

```bash
django-admin startproject first_app_tuto first_app
```

## Project archi:

- `manage.py`: CLI for the Django App
- `first_app_tuto`: directory with the actual package of the project
- `first_app_tuto/__init__.py`: tells python this a package
- `first_app_tuto/settings.py`: settings of the django app
- `first_app_tuto/urls.py`: URLs declarations for the project
- `first_app_tuto/asgi.py`:
- `first_app_tuto/wsgi.py`:
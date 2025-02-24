# Create a Virtual Environment 
```powershell   
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
pip install Django psycopg2-binary
```

# Django Development Process 
## Initialization 
Create an app in a project adding models, views, templates and urls 

## Core Development 
Create models -> Create views -> Map URLs -> Build UI -> Testing

## Add-ons 
Admin site + Security + 3rd party frontend + configuration + localization + logging

## Deployment and Monitoring 
Performance + Packaging and deployment


# Create a Django Project 
```bash 
$ django-admin startproject mysite
``` 

## Create an app 
```bash 
$ python manage.py startapp app_name
```
After creating the app we have to add it into the `INSTALLED_APPS` in settings.py

## Setup Database

To configure a database in Django, follow these steps:

1. **Install the database adapter**:
    For PostgreSQL, you need to install `psycopg2-binary`:
    ```bash
    pip install psycopg2-binary
    ```

2. **Update `settings.py`**:
    Modify the `DATABASES` setting in your `settings.py` file to configure the PostgreSQL database:
    ```python
    DATABASES = {
         'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'your_db_name',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost', # database host
              'PORT': '5432', # Default PostgreSQL port
         }
    }
    ```

3. **Apply migrations**:
    Run the following commands to apply migrations and create the necessary database tables:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a superuser**:
    Create a superuser to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:
    Start the development server to verify the database setup:
    ```bash
    python manage.py runserver
    ```


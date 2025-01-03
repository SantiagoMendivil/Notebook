# Table of contents
- [Table of contents](#table-of-contents)
- [Project Organization (Configurations)](#project-organization-configurations)
  - [Steps for Organizing Applications](#steps-for-organizing-applications)
  - [Steps for Organizing Urls Between Applications](#steps-for-organizing-urls-between-applications)
  - [Steps for Using the Models in the Django Admin](#steps-for-using-the-models-in-the-django-admin)
  - [Steps for Personalizing the Admin](#steps-for-personalizing-the-admin)
- [Steps for Using a Rest Service (simple)](#steps-for-using-a-rest-service-simple)
- [Organizing Software Environments](#organizing-software-environments)

# Project Organization (Configurations)
What we are expecting here is to organize a Django project on a way that we divide the applications from each other and also divide the development environment from the production environment. 

## Steps for Organizing Applications 
1. Create a directory called `applications` at the same level as `manage.py`.
2. Inside the directory create a `__init__.py` file. 
3. Go into the application and inside the virtual environment and create the necessary applications (`django-admin startapp appName`). 
4. Go into the file `settings.py` from the root project. 
5. In `INSTALLED_APPS` call `applications` and with a dot call the application name and then the configuration that is on the apps.py within the new application, for example `applications.book`
6. In order to avoid problems with the new path that the application has, go into the apps.py withing the new application and add the directory name before the name, for example if the new application's name is `book` the name inside the `BookConfig` will be `applications.book`.

## Steps for Organizing Urls Between Applications
1. In every new application we have to create a new `urls.py`
2. We have to call the urls.py from the new application by first importing `include` and then calling for example `path('', include('applications.applicationName.urls')), name='some_name'`
3. As we are using a name keyword we have to call the same name in the application's urls.py using `app_name='some_name'` as a new variable outside the urlpatterns

## Steps for Using the Models in the Django Admin
1. Create the models for your application
2. Run the command `python manage.py makemigrations`
3. Run the command `python manage.py migrate`
4. Create a superuser with `python manage.py createsuperuser`
5. Import the models from the `.models` file

## Steps for Personalizing the Admin
**Quick Note**: Django includes a decorator in order to avoid writing the typical command of `admin.site.register`. This decorator is called in the following syntax: 

```python 
@admin.register(ModelName)
class ModelNameAdmin(admin.ModelAdmin):
  pass
```


1. Create a class called `ModelNameAdmin` where model name is the model's name that you register
2. It must heritate from `admin.ModelAdmin`
3. It can use the decorator of `@admin.register(ModelName)` but it's not necessary, you can also use the models by calling the `admin.site.register(ModelName)`


# Steps for Using a Rest Service (simple)
1. Have already installed Django Rest Framework. 
2. In `views.py`: 
   1. import `generics` from `rest_framework`
   2. In the class that we'll define heritate from `generics.ListAPIView`
   3. Add queryset for the new class imported from models
   4. Add a serializer_class attribute that tells which serializer will be used in that view. 
   5. The serializer must be created heritating from serializers.ModelSerializer which is imported from rest_framework
   6. Add to the serializer a `class Meta` for including the model and the fields that you want from the serializer. 
3. In `urls.py`: 
   1. Call the `as_view()` method in order to transform the class to a view function. 

A final example would look like this: 

```python
# views.py 
from django.shortcuts import render
from .models import Book, Author, Editorial

# rest_framework
from rest_framework import serializers, generics

# Create your views here.


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

```python
# urls.py
from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('', BookList.as_view(), name='books'),
]
```


# Organizing Software Environments 
**Important in this section**: This section follows a technique where you work the configuration inside the project itself and not in the whole directory that also includes the env folder. 

1. Create a directory called requirements
2. Inside of the requirements directory create a `local.txt` file in order to save all the dependencies for a local environment
3. Create a `test.txt` file and a `prod.txt` in order to save the testing dependencies and the production dependencies. 
4. Inside of the django project, at the same level of settings.py, create a new directory called `settings` with a `base.py` file that will share all the common configurations among the project; `local.py` and `prod.py` that their names explain what they are for. 
5. In `base.py`
   1. As we created a new settings directory, we need to change the BASE_DIR variable in order to read the correct direction. 
   2. The INSTALLED_APPS will be destructured into three lists: LOCAL_APPS, DJANGO_APPS and THIRD_PARTY_APPS 
6. In order to read the new `local.py` we need to run the following command: `python manage.py runserver --settings=project_name.settings.local`. The keyword local means the environment in which the project is running.
7. In order to avoid writing all that command, we can edit the file `manage.py` and in the section where it says the project name with .settings, add the environment configurations name that we want. 
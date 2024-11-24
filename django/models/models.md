# Table of contents 
- [Table of contents](#table-of-contents)
- [Models](#models)
  - [Using a Different Backend](#using-a-different-backend)
  - [Creating a Model](#creating-a-model)
- [Structure of Model Class](#structure-of-model-class)
- [Migrate the Database](#migrate-the-database)
- [Admin Interface](#admin-interface)
- [Basic Implementation of Various Models](#basic-implementation-of-various-models)
- [Built-in Validations](#built-in-validations)
  - [Null](#null)
  - [Blank](#blank)
  - [db\_column](#db_column)
  - [Default](#default)
  - [help\_text](#help_text)
  - [primary key](#primary-key)

# Models
An essential part of any website is the ability to accept information from a user, input it into a database, retrieve information from a database, and the retrieved information to generate content for the user. Models define the structure of the data stored in a database, including the field type, possibly their maximum size or default values. 

## Using a Different Backend 
In the `settings.py` we can edit the ENGINE parameter for DATABASE. That is where we would connect to a different backend, if we didn't want to use SQLite. 

```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Creating a Model
A model is just like a python class. 

```python 
from django.db import models 

class Category(models.Model):
  name = models.CharField(max_length=255)

class Product(models.Model): 
  name = models.CharField(max_length=255)
  stock = models.IntegerField()
  score = models.FloatField()

  """
    Types of on_delete:
      CASCADE: Deletes the product if the category is eliminated
      PROTECT: Returns an error restricting the category elimination
      RESTRICT: It deletes only if there are no products
      SET_NULL: Updates to null value
      SET_DEFAULT: Assigns a default value
  """
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

```

# Structure of Model Class 
Here is an example of how to use a model for a Post on a social media app 

```python
from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.Charfield(max_length=255)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return f"{self.title} from {self.author}"
```


# Migrate the Database
After we defined the database using models, we can migrate the database. This lets Django do the heavy lifting of creating SQL tables that correspond to the models we just created. Migrating the database is a very useful function of Django because we only have to write those classes, and then with a single command, Django will automatically create a SQL database for us. 

```bash 
python manage.py migrate
```

After this, we can register the changes to our application with the following command: 
```bash 
python manage.py makemigrations my_app
```

We then migrate the database one more time with the same first command 
```bash
python manage.py migrate
```

# Admin Interface
Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn't require much creativity. The admin interface is one of the key features of Django, since we can get a full admin interface automatically.

In order to use this convenient admin interfae with the models, we need to register them to our applications's admin.py. 

```python 
from django.contrib import admin 
from app.models import Blog, User

admin.site.register(Blog)
admin.site.register(User)
```

In order to access the admin interface we have to create a superuser in the terminal 

```bash 
python manage.py createsuperuser
```


# Basic Implementation of Various Models 
```python 
class Topic(models.Model):
  top_name = models.Charfield(max_length=255, unique=True)

  def __str__(self):
    return self.top_name


class Webpage(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, unique=True)
  url = models.URLField(unique=True)

  def __str__(self):
    return self.name


class AccessRecord(models.Model):
  name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
  date = models.DateField()

  def __str__(self):
    return str(self.date) 
```


# Built-in Validations
## Null 
If True, Django will store empty values as NULL in the database/ Default is False. 
If True, the field is allowed to be blank. Default is False. 

## Blank 
If True, the field is allowed to be blank. Default is False. 

## db_column
The name of the database column to use for the field it is applied to. If this isn't 
given, Django will use the field's name. 

## Default 
The default value for the field. This can be a value or a callable object. If callable,
it will be called every time a new object is created. 

## help_text
Extra "help" text to be displayed with the form widget. This is useful for
documentation even if our field isn't used on a form. 

## primary key
If True, this field is the primary key for the model. 


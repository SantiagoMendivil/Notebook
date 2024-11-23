# Table of contents 
- [Table of contents](#table-of-contents)
- [Models](#models)
  - [Using a Different Backend](#using-a-different-backend)
  - [Creating a Model](#creating-a-model)
  - [](#)

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

## 
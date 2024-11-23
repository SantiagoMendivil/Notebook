# Table of contents 
- [Table of contents](#table-of-contents)
- [Models](#models)
  - [Using a Different Backend](#using-a-different-backend)

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
In order to create a django model
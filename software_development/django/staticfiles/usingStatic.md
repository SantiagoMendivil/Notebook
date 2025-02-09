# Table of contents 
- [Table of contents](#table-of-contents)
- [Static Files](#static-files)
  - [Step 1: Create a static directory](#step-1-create-a-static-directory)
  - [Step 2: Tell django where to find static](#step-2-tell-django-where-to-find-static)
  - [Step 3: Load static](#step-3-load-static)

# Static Files 
Static files are files that clients download as they are from the server or files that get served statically, i.e. with no modification. These static files could include stylesheets, JavaScript files, and images.


## Step 1: Create a static directory 
We have to create a directory by the name of static in the outermost project. Inside this directory, we will create a app_name directory, just like in the templates section of this notebook. 

```
project/
|-- project/
|-- app_name/
|-- templates/
|-- static/
    |-- app_name/
        |-- css/
        |-- js/
        |-- images/
```

## Step 2: Tell django where to find static
We have to edit settings.py file. We will use again the os.path.join to specify the static directory. So we add the following line below the TEMPLATE_DIR line: 

```python 
STATIC_DIR = os.path.join(BASE_DIR,"static")
```
This line of code makes the `STATIC_DIR` hold the absolute path to the location of the static folder inside of our project.

Then add a `STATIC_URL` that will hold the name of the static folder and assign `/static/` 

Then add `STATICFILE_DIRS` lists
```python
STATICFILES_DIRS = [
   STATIC_DIR,
]
```


The final code would look like this: 

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILE_DIRS= [
    STATIC_DIR,
]
``` 

## Step 3: Load static 
In whatever file you want to use an element from static your must add at the beginning of the file a tag that displays the following line of code: 
```html 
{% load static %}
```
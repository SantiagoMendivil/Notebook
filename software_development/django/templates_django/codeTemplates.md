# Table of contents
- [Table of contents](#table-of-contents)

# Code Templates in Django 
Step by step on how to create the templates directory in order to configure it well. 

## Step 1: Create a templates directory 
First we have to create a **templates** directory in the outermost project directory. Then inside templates directory we will add another directory by the name of our application or applications.

`project/templates/app_name`

```
project/
|-- project/
|-- app_name/
|-- templates/
    |-- app_name/
```

## Step 2: Tell django where to find templates 
We have to use the os module to feed path to the DIR key. In `settings.py` in our projects directory, we will se a BASE_DIR variable. This builds the paths inside of the project. We can user BASE_DIR to refer to the templates directory. 

```python
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
```
This will hold the absolute path to the location of the templates folder inside the project. 

Then we have to specify this variable in the `TEMPLATES` list in `settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
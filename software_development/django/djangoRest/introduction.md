# Table of contents
- [Table of contents](#table-of-contents)
- [How It Works? (Just a general description)](#how-it-works-just-a-general-description)
- [Installing Django Rest](#installing-django-rest)

# How It Works? (Just a general description)
A server processes the information which is defined in a JSON file and exports it to any device that needs that information in order to be manipulated by every language without compatibility problems. 

For example if we are using a model named User, a JSON file (it can be also an XML file) that will hold the information can be something like this: 

```json 
{
    {
    "name": "Santiago", 
    "age": "20", 
    "career": "Software Engineering",
    }
}
```

# Installing Django Rest
1. Run the following command in the terminal `pip install djangorestframework`
2. Add the package into the INSTALLED_APPS: `'rest_framework'`


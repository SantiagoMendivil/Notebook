# Table of contents 
- [Table of contents](#table-of-contents)
- [Template Inheritance](#template-inheritance)
  - [Parent template file](#parent-template-file)
  - [Using includes/](#using-includes)
- [block tags](#block-tags)

# Template Inheritance
Template inheritance is the most powerful and complex part of Django’s template engine. It allows us to build a base “skeleton” template that contains all of the common elements of our site, and defines blocks that child templates can override.

it saves us a lot of repetitive work and makes it much easier to maintain the same base look and feel across our entire website. 

## Parent template file 
The parent template is usually named base.html, but it can be anything. It will look something like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>{% block title %} <!-- Title Name -->  #}{% endblock %}</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
</head>
<body>

<nav class="navbar navbar-default navbar-static-top">
  <div class=container>
    <ul class= "nav navbar-nav">
      <li class="active"><a class="navbar-brand" href="{% url 'home' %}">Home</a></li>
      <li><a class="navbar-brand" href="{% url 'search' %}">Search</a></li> 
      <li><a class="navbar-brand" href="{% url 'admin' %}">Admin</a></li>
    </ul>
  </div>
</nav> 

  
<div class="container">
  {% block content %}<!-- Page content   -->{% endblock %}
</div>

</body>
```

In this example the tag that says `block title` and `block content` will display the elements that you specify in another template. 

## Using includes/
We can define a directory called `includes/` that will hold also blocks of code separately from the base, like the navbar or the footer. 

The structure could be something like this: 
```
project/
|-- project/
|-- app_name/
|-- templates/
    |-- app_name/
    |-- includes/
        |-- navbar.html
        |-- footer.html
    |-- base.html 
```

And then in order to render that includes in the base we can access them like the following example: 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>{% block title %} <!-- Title Name -->  #}{% endblock %}</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
</head>
<body>

{% include "includes/navbar.html" %}
  
<div class="container">
  {% block content %}<!-- Page content   -->{% endblock %}
</div>

{% include "includes/footer.html %}

</body>
``` 


# block tags 
These block tags tell the template engine that a child template may override those portions of the template.

A template that inherits from base.html will look like this for the home page for example: 

```html
<!DOCTYPE html>
{% extends "base.html" %}

{% block title %} Home {% endblock %}

{% block content %}

<h3>Welcome to Home Page</h3>

{% endblock %}
``` 

The `extends` tag is important because it tells the template engine that this template "extends" another template. At that point, the template engine will notice the two block tags in base.html and replace those blocks with the contents of the child template, which is the home.html file.

In base.html, where the block content tags are empty, will be replaced by the ones that are extending that file. 
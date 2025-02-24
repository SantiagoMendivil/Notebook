# Table of contents
- [Table of contents](#table-of-contents)
- [Templates](#templates)
- [Django Template Language](#django-template-language)

# Templates 
 A template contains the static parts of the desired HTML output, as well as some special syntax describing how dynamic content will be inserted. We can think of the template as the scaffolding or skeleton of the page.

 # Django Template Language
 The Django template language is designed to feel comfortable for those who are already familiar with HTML. 

 A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else in the output will remain the same.
 
 The syntax of the Django template language involves four constructs:

- Variables
- Tags
- Filters
- Comments


```html 
{% extends "base_generic.html" %}

{% block title %}{{ page.title }}{% endblock %}

{% block content %}
<h1>{{ page.title }}</h1>

{% for blog in blog_list %}
<h2>
  <a href="{{ blog.get_absolute_url }}">
    {{ blog.header|upper }}
  </a>
</h2>
<p>{{ blog.body|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
```
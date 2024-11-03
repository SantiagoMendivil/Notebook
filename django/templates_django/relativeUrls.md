# Table of contents
- [Table of contents](#table-of-contents)
- [Relative URLs](#relative-urls)
- [url tag](#url-tag)
  - [Referencing a specific path from an specific application](#referencing-a-specific-path-from-an-specific-application)

# Relative URLs 
Traditionally, when we use an anchor tag with an href, we have to pass in the hardcoded path to the file. However, this method is not suitable if we want our Django project to work on any system. So let’s see how to replace a hardcoded URL path in an href with a URL template.

# url tag 
The best way to replace a hardcoded URL path in a Django template is to use the url tag. The syntax for the url tag is as follows:

```html
{% url 'url_name' arg1=v1 arg2=v2 %}
```
For example, if we had the following URL:
```html
<a href= "/profile/12" >Profile</a>
```

We can modify it to structure it in the `urls.py` and then call it: 
```python
path('/profile/<int:id>', views.profile, name='show-profile')
```

```html
<a href = "{% url 'show-profile' id=12 %}">Profile</a>
```

## Referencing a specific path from an specific application
```html
{% url 'my_app:index' %}
```

In this example we have to set the app_name inside the `urls.py` and assign a string with the name of the applications name. 
# Table of contents 
- [Table of contents](#table-of-contents)
- [Django Applications](#django-applications)
  - [Pluggable Django applications](#pluggable-django-applications)
  - [Running again the application](#running-again-the-application)
- [Static and Dynamic Routing](#static-and-dynamic-routing)
  - [Static routing](#static-routing)
  - [Dynamic routing](#dynamic-routing)
    - [Dynamic routing with path converters](#dynamic-routing-with-path-converters)
- [URL Mappings](#url-mappings)
  - [include() function](#include-function)

# Django Applications 
A django application is created to perform a particular function for a Django project. For example, a project could have a registration application, a comments application, a polling application, etc. 

## Pluggable Django applications 
These Django applications can be plugged into other Django projects, so we can reuse them or use other people's applications in out project 

```bash 
python manage.py startapp <app_name>
```

## Running again the application
- Add the <app_name> to the settings.py inside of the INSTALED_APPS list. Just add a string that represents the app's name 
- Add a view in the <app_name/views.py>. 
- Map a view to a URL by importing the views in <app_name/urls.py> and then defining an urlpatterns list. 

# Static and Dynamic Routing
## Static routing
In static routing, we specify a constant URL string as a path in the urls.py file.

## Dynamic routing 
To add a variable in path, we use it bewteem the angle brackets. For example <question_id>.

### Dynamic routing with path converters 
- str: Matches any non-empty string, excluding for us to use 
- int: Matches zero or any positive integer
- slug: Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-1st-django-site
- uuid: Matches a formatted UUID
- path: Matches any non-empty string, including the path separator, '/' this allows us to match against a complete URL path rather than a segment of a URL, as with str. 

# URL Mappings 
## include() function 
The include() allows us to look for a match with the path defined in the urls.py file of our project, and link it back to our application's own urls.py
# Table of contents
- [Table of contents](#table-of-contents)
- [Project Organization (Configurations)](#project-organization-configurations)
  - [Steps for Organizing Applications](#steps-for-organizing-applications)
  - [Steps for Organizing Urls Between Applications](#steps-for-organizing-urls-between-applications)

# Project Organization (Configurations)
What we are expecting here is to organize a Django project on a way that we divide the applications from each other and also divide the development environment from the production environment. 

## Steps for Organizing Applications 
1. Create a directory called `applications` at the same level as `manage.py`.
2. Inside the directory create a `__init__.py` file. 
3. Go into the application and inside the virtual environment and create the necessary applications (`django-admin startapp appName`). 
4. Go into the file `settings.py` from the root project. 
5. In `INSTALLED_APPS` call `applications` and with a dot call the application name and then the configuration that is on the apps.py within the new application, for example `applications.book.apps`
6. In order to avoid problems with the new path that the application has, go into the apps.py withing the new application and add the directory name before the name, for example if the new application's name is `book` the name inside the `BookConfig` will be `applications.book`.

## Steps for Organizing Urls Between Applications
1. In every new application we have to create a new `urls.py`
2. We have to call the urls.py from the new application by first importing `include` and then calling for example `path('', include('applications.applicationName.urls')), name='some_name'`
3. As we are using a name keyword we have to call the same name in the application's urls.py using `app_name='some_name'` as a new variable outside the urlpatterns
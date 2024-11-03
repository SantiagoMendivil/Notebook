# Table of contents 
- [Table of contents](#table-of-contents)
- [Creating a Django project](#creating-a-django-project)
- [Running the project](#running-the-project)

# Creating a Django project 
A Django project is a collection of applications and configurations that, when combined together, will make up the full web application. 

```bash
mkdir project_name
cd project_name
code .
python -m venv env 
env/Scripts/activate
echo > requirements.txt
pip install -r requirements.txt
django-admin startproject <project_name>
```


# Running the project 
```bash 
python manage.py runserver
```

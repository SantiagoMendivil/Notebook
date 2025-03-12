# Table of contents
- [Table of contents](#table-of-contents)
- [Virtual Environment](#virtual-environment)
- [Virtual Environment in Python](#virtual-environment-in-python)


# Virtual Environment
A virtual environment is a small piece of storage in our computer that contains all the dependencies of a project apart from the computer itself. For example, if we are working in a django project in a lower version than 4, and we don't want trouble with the django version downloaded in a computer, we might use a virtual environment to avoid these conflicts. 

# Virtual Environment in Python
The command that creates a virtual environment in a project is the following: 

```shell 
python -m venv venv
```

In order to activate this command we use the following command: 

```shell 
env/Scripts/activate
```

You can deactivate the virtual environment by calling the following command: 

```shell
deactivate
```
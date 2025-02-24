# Table of contents 
- [Table of contents](#table-of-contents)
- [Singleton Pattern](#singleton-pattern)
  - [What is it?](#what-is-it)
  - [Class Diagram](#class-diagram)
  - [Example in Python](#example-in-python)
  - [Example in Django](#example-in-django)

# Singleton Pattern
## What is it? 
Singleton pattern as the name suggests is used to create one and only instance of a class. There are several examples where only a single instance of a class should exist and the constraint be enforced. Cahces, thread pools, registries are examples of objects that should only have a single instance. 

Formally the Singleton pattern is defined as ensuring that only a single instance of a class exists and a global point of access to it exists. 

## Class Diagram 
![Class Diagram for Singleton Pattern](images/image2.png)

## Example in Python

Here is an example of the Singleton pattern implemented in Python:

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

# Usage
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
```

In this example, the `SingletonMeta` class is a metaclass that ensures only one instance of the `Singleton` class is created. The `__call__` method is overridden to control the instance creation process.

## Example in Django

Here is an example of applying the Singleton pattern in a Django project to manage a configuration object:

```python
# myapp/singleton.py
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.load_config()

    def load_config(self):
        self.config = {
            'setting1': 'value1',
            'setting2': 'value2',
        }

    def get_config(self):
        return self.config
```

You can use this singleton class in your Django views or other parts of your application as follows:

```python
# myapp/views.py
from django.http import JsonResponse
from .singleton import AppConfig

def config_view(request):
    config = AppConfig.get_config()
    return JsonResponse(config)
```

In this example, the `AppConfig` class is a singleton that loads and provides access to application configuration settings. The `config_view` function in `views.py` uses this singleton to return the configuration as a JSON response.
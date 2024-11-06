# Table of contents
- [Table of contents](#table-of-contents)
- [Prototype Pattern](#prototype-pattern)
- [Class diagram](#class-diagram)
- [Example in a Django Project](#example-in-a-django-project)
  - [models.py](#modelspy)
  - [Usage](#usage)

# Prototype Pattern 
Formally, the pattern is defined as specify the kind of objects to create using a prototypical instance as a model and making copies of the prototype to create new objects.

Imagine a class will only be loaded at runtime and you can't access its constructor statically. The run-time environment creates an instance of each dynamically loaded class automatically and registers it with a prototype manager. The application can request objects from the prototype manager which in turn can return clones of the prototype.

# Class diagram 
![Class diagram for Prototype Pattern](images/image3.png)

# Example in a Django Project
We will create a prototype for a `Product` model and clone it to create new instances.

## models.py

```python
from django.db import models
import copy

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def clone(self):
        return copy.deepcopy(self)
```

## Usage

```python
from .models import Product

# Create an original product
original_product = Product(name="Original Product", price=99.99, description="This is the original product.")
original_product.save()

# Clone the original product
cloned_product = original_product.clone()
cloned_product.name = "Cloned Product"
cloned_product.save()

print(f"Original Product ID: {original_product.id}, Name: {original_product.name}")
print(f"Cloned Product ID: {cloned_product.id}, Name: {cloned_product.name}")
```

In this example, we define a `clone` method in the `Product` model that uses Python's `copy.deepcopy` to create a deep copy of the instance. This allows us to create a new instance of `Product` with the same attributes as the original but with a different identity.
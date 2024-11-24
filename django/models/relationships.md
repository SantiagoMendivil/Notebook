# Table of contents 
- [Table of contents](#table-of-contents)
- [Many To One Relationship](#many-to-one-relationship)
- [Many to Many Relationship](#many-to-many-relationship)
- [One to One Relationship](#one-to-one-relationship)

# Many To One Relationship 
The ForeignKey field is used for a Many-to-One relationship. To undestrand how this relationship between models work, let's create two simple models. 
- Company 
- Employee

Basically the relationship between these two models is that an employee works at one company, and a company provides work to many employees. 
The implementation for these two models would be the following: 

```python 
from django.db import models
from datetime import date 


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number_of_employees = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.employee_name
```

# Many to Many Relationship 
We can implement this kind of relationship by adding a new model to our previous example. This new model is Projects. Basically the relationship would be that a project can have many employees enrolled to them, and the employees can enroll to many projects. 

The model implementation would be something like this: 

```python 
from django.db import models
from datetime import date 


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number_of_employees = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.employee_name


class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True)
    employee_name = models.ManyToManyField('Employee')

    def __str__(self):
        return self.project_name
```


# One to One Relationship
In order to understand better this relationship we can go back to the previous example. We can add a relationship between a project and the emoloyees where a project can have a team leader and that team leader can only be at one project at a time. 
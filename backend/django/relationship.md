# Many to Many intermediate table 
When having a relationship of many to many, we can add a new table known as **intermediate table** which saves information of both tables that will be joined in the many to many relationship. 

For example a **Course** entity and a **Learner** entity may have an intermediate table called **Enrollment** where: 

```python 
class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    learners = models.ManyToManyField(Instructor, through="Enrollment")


class Enrollment(models.Model):
    course = models.ForeignKey(Course)
    learner = models.ForeignKey(Learner)
    date_enrolled = models.DateField()


class Learner(models.Model):
    occupation = models.CharField(max_length=20)
    social_link = models.URLField()
```

# Relationship: Inheritance 
Determine if parent models should have their own tables 
- **Multi-table**
  - Subclassing an existin model 
  - Each model will have a separate database table 
- **Abstract base classes**
  - Parent class to hold common information
  - No base table created 
- **Proxy models**
  - Modify the application-level behavior of a model from th withouth changing fields

Following the example above, the instuctor would inherit from User, having this relationship: 

```python 
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)


class Instructor(User):
    is_full_time = models.BooleanField()
    total_learners = models.IntegerField()
```


# Migrating the Database 
```bash 
python manage.py makemigrations app_name 

python manage.py sqlmigrate app_name 000n

python manage.py migrate
```


# Test if a model was succesfully created 
```python 
# tests.py
# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from orm.models import User
from datetime import date

# Delete all data
def clean_data():
    User.objects.all().delete()

# Test Django Model Setup
def test_setup():
    try:
        clean_data()
        # Create a test user and save to database
        user = User(first_name='John', last_name='Doe', dob=date(1970, 3, 16))
        user.save()
        # Check user table is not empty
        assert User.objects.count() > 0
        print("Django Model setup completed.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise(exception)
    except:
        print("Unexpected error")

test_setup()
```
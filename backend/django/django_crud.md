# Table of contents
- [Table of contents](#table-of-contents)
- [Retrieve: Find objects with filter](#retrieve-find-objects-with-filter)
- [Retrieve: Find objects with exclude and filters](#retrieve-find-objects-with-exclude-and-filters)
- [Retrieve a single object](#retrieve-a-single-object)
- [Find objects in related fields](#find-objects-in-related-fields)
- [Exception](#exception)
- [Deleting Related Objects](#deleting-related-objects)

# Retrieve: Find objects with filter 
When using the `filter()` method we can add parrameters like: 

- field_name +_+
- query expression 
- __gt, __lt, __gte, __lte
- __contains, __startswith, __endswith 
- in 
- isnull

Here are some examples of using the `filter()` method:

```python
# Example 1: Filter objects where the field 'age' is greater than 25
adults = Person.objects.filter(age__gt=25)

# Example 2: Filter objects where the field 'name' contains 'John'
johns = Person.objects.filter(name__contains='John')

# Example 3: Filter objects where the field 'created_at' is not null
non_null_dates = Event.objects.filter(created_at__isnull=False)

# Example 4: Filter objects where the field 'status' is either 'active' or 'pending'
active_or_pending = Task.objects.filter(status__in=['active', 'pending'])

# Example 5: Filter objects where the field 'price' is less than or equal to 100
affordable_items = Product.objects.filter(price__lte=100)
```

# Retrieve: Find objects with exclude and filters
When using `exclude()` method it returns a QueySet that does not match the given lookup parameters. We can add an `AND` operator by calling the filter method with a dot. 

```python 
filtered_instructors = Instructor.objects.exclude(full_time=False).filter(total_learners__gt=30000).filter(first_name__startswith="J")
```

Another option is to add the filters in the same method but separated by commas. 

# Retrieve a single object
Use the `get()` method to retrieve only one record. 

# Find objects in related fields 
When working with foreign keys we can query elements related by calling the foreign table on the query. for example if we have these models: 

```python 
class Course(models.Model):
    instructors = models.ManyToManyField(Instructor)

class Instructor(models.Model):
    pass
```

We can get, for example, the courses with instructor's first name "John". 

```python 
courses = Course.objects.filter(instructors__first_name="John")
```
Notice that the field name of each related field is separated by double underscores. 


# Exception 
When trying to retrieve data, we can enclose the query between a try clause and the exception would be `Model.DoesNotExist`


# Deleting Related Objects 
- **CASCADE**: Also deleting all referencing objects 
- **PROTECT**: Prevent the object from being deleted if it has any objects related. 
- **SET_NULL**: Leave the related objects, only possible if the main object can be null. 
- **SET_DEFAULT**: Assign a related object to a default main object
- **SET()**: Assign related objects to a specific main object different than the one being deleted. 
- **DO_NOTHING**: Literally does nothing ?.



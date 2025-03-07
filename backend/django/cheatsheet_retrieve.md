# count()
Counts the number of objects 

```python 
Model.objects.count()
```
# Sum()
Provides the sum of a field
```python 
Model.objects.aggregate(Sum('field'))
```
# Avg()
Calculares the average of a field 

```python 
Model.objects.aggregate(Avg('field'))
```
# Max()
Provides the maximum value of a field

```python 
Model.objects.aggregate(Max('field'))
```
# Min()
Provides the minimum value of a field 
```python 
Model.objects.aggregate(Min('field'))
```
# order_by()
Orders objects based on a field 
```python 
Model.objects.order_by('field')
```
# order_by(-)
Order objects based on fields in descending orders
```python 
Model.objects.order_by('-field')
```
# select_related()
Performs inner join
```python 
Model.objects.select_related('related_model')
```
# prefetch_related()
Performs left Outer join
```python 
Model.objects.prefetch_related('related_model')
```
# many_to_many()
Performs many-to-many join
```python 
Model.many_to_many.all()
```
# filter(ForeignKey)
Performs conditional joins
```python 
Model.objects.filter(related_nodel__isnull=True)
```

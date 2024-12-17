# Table of contents 
- [Table of contents](#table-of-contents)

# Django Forms
We have to create a new file called `forms.py`. 

Then we need to import forms from Django and define the forms that we want to implement in our system there. 

```python 
from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()
```
# Render a Form 

## Step 1. Make a view for a form
In order to render a form we have to first define a view for the form in `views.py`

```python 
from .forms import SearchForm

def forms(request):
    form = SearchForm()
    return render(request, "app/forms.html", {'form': form})
```

Here there are some things to have in mind when creating a view. In order to render the form we have to import it from the forms and then initialize it as the class it is with a variable name. Then we just pass it into the template as context. 


## Step 2. Make a template to render the form
In this step, we have to create a file forms.html or the name that we give to the html in the view. Then we have to put the html inside. 

```html 
<form method="GET" action="https://google.com"> 
    {{ form }}
    <input type="submit" value="Search">
</form>
```

## Step 3. Make a URL for that Form 
In the same application as the views we have to define the url in order to the user to access the view. 

```python 
path('forms/', views.forms, name="form"), 
```


# Collecting Data via Django Form 
## Step 1. Grab data from the form 
We need to write some code so we can grab data from out POST request. Let's see the code first: 

Suppose the new form is this one: 
```python
class TestForm(forms.Form):
    text = forms.CharField() 
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()

```

```python 
def forms(request):
    form = TestForm( request.POST or None)
    data = "None"
    text= "None"
    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get("text")
    return render(request,'first_app/forms.html', {'form': form,'data': data, 'text': text})
```

In this case when we pass the fields for the form, the data will be passed as json object and the text in this case will be what is passed in the field text. 


# Form Validation
Django form fields have built-in validation in them. However, we can pass some optional arguments to validate them according to our own requirements. 

This validation should be written inside of the form class. 

```python

class TestForm(forms.Form):
    text = forms.CharField() 
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()

    def clean_integer(self):
        integer= self.cleaned_data.get("integer")
        if integer <= 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer
```

The validations must always have the clean keyword before the name of the attribute to validate. 

# Initialize the Values for the Form 
In order to initialize the form, inside the views we must declare a dictionary with the data we want to render and then pass it as an argument. In this case, it will be something like this: 

```python
def forms(request):
    inital_dict={
        "text": "Some initial data",
        "integer": 123,
    }
    form = TestForm( request.POST or None,initial=inital_dict)
    data = "None"
    text= "None"
    if form.is_valid():
        data = form.cleaned_data
        text= form.cleaned_data.get("text")
    return render(request,'first_app/forms.html', {'form': form,'data': data, 'text': text})
```

Here we apply the argument `initial` in order to receive the dictionary by default to fill the form. 

Also we can instead of passing the dictionary directly to the view, we can add it inside the `TestForm`. 


# Form Field Widgets and Labels

## How to customize widgets 
A widget in django is the HTML representation of a form field. By default, each Django form field works with a specific type of widget. For example, when we selected the integer field, we render an integer widget. 

### Textarea widget 
The following will provide us with a textarea widget: 

```python 
text = forms.CharField(min_length=7, widget=forms.Textarea)
```

### Select widget
The widget allows us to select an option from different choices. For this work, we first need to make those different choices. So we can do the following: 

```python 
INTS_CHOICES = [tuple([x, x]) for x in range(0,100)]

integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS_CHOICES))
```

### RadioSelect widget
This widget allows us to select option in terms of radio buttons. Let's make another array of tuples for this one: 

```python 
RADIO_CHOICES = [
    ('signin', 'Sign In'),
    ('signup', 'Sign Up'),
    ('forgotpassword', 'Forgot Password')
]

radio_choices = forms.CharField(min_length=4, widget=forms.RadioSelect(choices=RADIO_CHOICES))
```


### CheckboxSelectMultiple
This widget is used to check option from different checkboxes. 

```python 
CHECKBOX_CHOICES = [
    ('terms', 'Agree to terms and conditions'),
    ('privacy', 'Agree to privacy policy'),
]

checkbox_choices = forms.CharField(min_length=4, widget=CheckboxSelectMultiple(choices=CHECKBOX_CHOICES))
```


### SelectDateWidget widget 
This widget allows us to select a particular date. It makes it very easy for us to set a specific date or time for a particular thing. By default, it only comes up with a few years, but we can give the widget our own range of years. 

```python 
YEARS= [x for x in range(1980,2031)]

date_field= forms.DateField(initial="2020-20-5",widget=forms.SelectDateWidget(years=YEARS))
```


# Model Form 
Usually, if we have a model in our application, we will also have a form associated with it. The form would be responsible for creating new instances of the model. Instead of creating a separate form and adding each field again, Django has provided us with a simplified method using the model forms. 

## Step 1. Create a model
Since we already know how to set up a model, we won't be creating one from scratch. Instead we will use this one: 

```python 
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
```

## Step 2. Migrate the database and create a superuser

## Step 3. Create a model form 

```python 
class PostModelForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields= ["user","title","slug","image","content","draft","publish"]
        exclude= []
```
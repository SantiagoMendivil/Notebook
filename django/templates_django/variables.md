# Table of contents 
- [Table of contents](#table-of-contents)
- [Variables](#variables)
- [How to use variables](#how-to-use-variables)

# Variables 
A template contains variables, which get replaced with values when the template is evaluated.

A variable looks like this: `{{ variable }}`.

Variable names consist of any combination of alphanumeric characters and the underscore (_), but they may **not** start with an underscore.

Use a dot `(.)` to access the attributes of a variable.

# How to use variables 
We use variables inside the templates by passing any Python object to the `render()` function.

```python
return render(request, "index.html", context=context_object)
```


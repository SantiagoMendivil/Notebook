# Table of contents 
- [Table of contents](#table-of-contents)
- [Tags](#tags)
- [for tag](#for-tag)

# Tags 
Tags look like this: `{% tag %}`. Tags are more complex than variables: some create text in the output, some control the flow of the template using `for` loops or `if-else`, and some load external information into the template which is used by later variables.

# for tag 
This is used to loop over each item in an array or any similar data structure

```html 
<ul>
{% for element in name_of_list %}
    <h4>{{ forloop.counter }}</h4>
    <li>{{ element }}</li>
{% endfor %}
</ul>
```

The forloop.counter is the current index in the array


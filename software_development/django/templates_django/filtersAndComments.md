# Table of contents 
- [Table of contents](#table-of-contents)


# Filters 
Filters are used to modify variables for display

```html 
{{ variable | filter_name }}
```

A | (called as a **pipe**) is used to apply a filter. Basically, the syntax above will display the value of the {{ variable }} after being filtered through the filter_name filter. 

## default filter
This filter can be used when we are unsure if the variable is empty or not. For example:
```html 
{{ value|default:"Value not provided" }}
```

## length filter 
This filter returns the length of the variable. This works for both strings and lists. For example:
```html 
{{ value|length }}
```
If the value is a list of four elements, then the output will be 4. 

## lower filter 
This filter converts a string into all lowercase. For example: 
```html
{{ value|lower }}
```

## make_list filter
This filter will convert the value into a list by spliting each character or number. For example:
```html 
{{ value|make_list }}
```
If the value is **hello world** then it will convert it to ['h', 'e', 'l', 'l', 'o', '', 'w', 'o', 'r', 'l', 'd']

## title filter 
This filter will capitalize each beginning word on a value. For example:
```html
{{ value|title }}
```
If the value is **hello world** it will convert it to **Hello World**

## cut filter 
This filter will join each word in a value by eliminating the spaces between strings. For example: 
```html 
{{ value|cut }}
```
If the value is **hello world** then it will be **helloworld**


# Comments 
These are used to commet-out part of a line in a template. 

`{# This is a comment #}`
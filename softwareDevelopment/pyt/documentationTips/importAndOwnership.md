# Table of contents 
- [Table of contents](#table-of-contents)
- [Hello World](#hello-world)
- [Import this](#import-this)
- [Special functions](#special-functions)

# Hello World 
Python has literally a module named __hello__ that outputs "Hello world!" to the console without the necessity of printing something

```python
import __hello__
```

# Import this
The module contains The Zen of Python, a set of guiding principles that define the Pythonic programming style. 

```python 
import this
```

This would output
```bash
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

This is stored in the module as a scrambled string, this.s, that comes with a dictionary, this.d, for unscrambling.

In order to unscramble this we have to write the following line of code:

```python
''.join(this.d.get(x,x) for x in this.s)
```

# Special functions 
- `copyright()`: will display the copyrights of python 
- `credits()`: will display the names of those who contributed to python 
- `license()`: will display the legal status of python 


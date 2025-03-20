""" 
    Author: Santiago Mendivil Alvarez 
    
    Date: 2025-02-10
    
    Description: 
        This file contains the implementation of high order functions in Python. Using methods like map, filter, reduce, and the combination of them. 
        
    Definitions:
        Imperative code: Style of programming that focuses on explicitly 
        describing the steps to achieve a result. Uses loops and conditionals
        by default.
        
        Predicate: A function that returns a boolean value.
        
        Declarative code: Style of programming that focusess on what 
        the result should be, rather than how to achieve it. Functions
        like filter, map or reduce are used to express these operations.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = filter(lambda x: x % 2 == 0, nums)
print(tuple(filtered_numbers))

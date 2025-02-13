""" 
    Author: Santiago Mendivil Alvarez 
    
    Date: 2025-02-10
    
    Description: 
        This file contains the implementation of high order functions in Python. Using methods like map, filter, reduce, and the combination of them. 
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = filter(lambda x: x % 2 == 0, nums)
print(tuple(filtered_numbers))

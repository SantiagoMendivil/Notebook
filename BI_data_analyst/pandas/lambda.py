""" 
    A function is an object that is able to accepts some sort 
    of input, possibly modify it, and return some sort of output.
    A lambda function is a small anonymous function.
"""


def add_two(my_input): return my_input + 2


print(add_two(3))
print(add_two(100))
print(add_two(-2))

"""  
    Syntax
        - The function is stored in a variable
        - lambda declares that is a lambda function
        - The input is what we call in the parenthesis 
        - The return is what we want to use the input for
"""

# Function that checks if a string is a substring of the string


def is_substring(my_string): return my_string in "Hello world"
def is_substring(my_string): return my_string in "This is the master string"


def check_if_A_grade(
    grade): return 'Got an A!' if grade >= 90 else 'Did not get an A...'

""" 
    Using conditionals in lambda:
        long_string = lambda str: True if len(str) > 12 else False
        
    Modifying using conditionals in lambda:
        double_or_zero = lambda num: num * 2 if num > 10 else 0
        
        even_or_odd = lambda num: "even" if num%2==0 else "odd"
        
        rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"


    You can use the modulo operator with 10 to find the ones' places of an integer
        one_place = lambda num: num%10
        
    Using Random:
        random.randint(a, b): Returns an integer between a and b
        
        
"""

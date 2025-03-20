# Table of contents
- [Table of contents](#table-of-contents)
- [Advanced naming considerations](#advanced-naming-considerations)
- [The anatomy of an exemplary docstring.](#the-anatomy-of-an-exemplary-docstring)
  - [Arguments](#arguments)
  - [Return values](#return-values)
  - [Exception handling](#exception-handling)
  - [Example](#example)
- [Functions best practices](#functions-best-practices)
  - [Function length](#function-length)
  - [The art of decomposition](#the-art-of-decomposition)
    - [Multiple responsibilities.](#multiple-responsibilities)
    - [Cognitive overload](#cognitive-overload)
    - [Testability](#testability)

# Advanced naming considerations
If a function is intended for internal use within a module and shouldn't be accessed directy from outside, prefix its name with an underscore (_). For instance **_calculate_internal_metrics**. 

Functions that return a boolean value, strongly consider using prefixes like **is_**, **has_**, **can_**. 


# The anatomy of an exemplary docstring. 
## Arguments
A detailed list of all input parameters including:

- Clear and descriptive names that match the function's internal variables
- The expected data types of each argument
- Brief explanations of what each argument represents and how it's used.
- An indication of whether each argument is optional or mandatory. If optional, provide default values. 

## Return values
A clear description of the data type and meaning of the value returned by the function. If the function doesn't return anythin, state it explicitly. 

## Exception handling
Strengthen the use of raises in docstrings by specifying exceptions and why they are raides. 

## Example 
```python 
def calculate_monthly_payment(principal: float, interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the monthly payment for a fixed-rate loan.

    Args:
        principal (float): The total amount borrowed.
        interest_rate (float): The annual interest rate (as a decimal, float).
        loan_term_years (int): The loan term in years.

    Returns:
        The monthly payment amount (float).

    Raises:
        ValueError: If any of the inputs are negative or zero.

    Example:
        >>> calculate_monthly_payment(100000, 0.05, 30)
        530.33 
    """
    if principal <= 0 or interest_rate <= 0 or loan_term_years <= 0:
        raise ValueError("All input values must be positive.")

    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term_years * 12
    
    # Calculation logic for monthly payment (omitted for brevity)

    return monthly_payment
```

# Functions best practices 
## Function length
A function should be concise yet complete. Typically around 10-20 lines of code in order to make them easier to digest and comprehend at a glance. 

## The art of decomposition
The **Single Responsibility Principle(SRP)** plays a pivotal role in determining when to decompose a function. The SRP states that a class or module should have only one reason to change. A function should do one thing and do it well. 

### Multiple responsibilities. 
If a function is juggling multiple tasks like fetching data, processing it and saving the results, it's violating the SRP principle. 

### Cognitive overload
Decomposition can make the logic more manageable and easier to follow, reducing cognitive load and improving code readability. 

### Testability
Long, convoluted functions are difficult to test thoroughly. Breaking them down into smalled, more focused units, you create functions that are easier to test in isolation. 


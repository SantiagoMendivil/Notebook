# Table of contents 
- [Table of contents](#table-of-contents)
- [Asymptotic Analysis](#asymptotic-analysis)
- [Big O Notation](#big-o-notation)
  - [Understanding Big O Notation](#understanding-big-o-notation)
    - [Simplified Asymptotic Analysis](#simplified-asymptotic-analysis)
    - [Common Functions and Their Growth Rates](#common-functions-and-their-growth-rates)
    - [Comparison of Common Functions](#comparison-of-common-functions)

# Asymptotic Analysis 
The asymptotic notation compares two functions, say f(n) and g(n) for very large vlues of n. This fits in nicely with our need for comparing algorithms for very large input sizes. 

# Big O Notation 
This is one of the asymptotic notations. A function f(n) is considered O(g(n)), read as big oh of g(n), if there exists some positive real constant c and integer n0 >= 0, such that the following inequality holds for all n >= n0. 

## Understanding Big O Notation

Big O Notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. It provides an upper bound on the growth rate of the function. This helps in understanding the worst-case scenario of an algorithm's performance.

### Simplified Asymptotic Analysis

In simplified terms, asymptotic analysis allows us to compare the efficiency of different algorithms by focusing on their growth rates. Instead of exact measures, we look at how the run time or space requirements increase with the size of the input. This helps in identifying the most scalable algorithms.

### Common Functions and Their Growth Rates

Here are some common functions used in Big O Notation, listed from fastest to slowest growth rate:

- **O(1)**: Constant time - The run time does not change with the size of the input.
- **O(log n)**: Logarithmic time - The run time grows logarithmically with the input size.
- **O(n)**: Linear time - The run time grows linearly with the input size.
- **O(n log n)**: Linearithmic time - The run time grows in proportion to n log n.
- **O(n^2)**: Quadratic time - The run time grows quadratically with the input size.
- **O(2^n)**: Exponential time - The run time grows exponentially with the input size.
- **O(n!)**: Factorial time - The run time grows factorially with the input size.

### Comparison of Common Functions

- **Logarithmic (O(log n))**: Algorithms with logarithmic time complexity are highly efficient, as they reduce the problem size significantly with each step. Examples include binary search.
- **Linear (O(n))**: Algorithms with linear time complexity scale directly with the input size. Examples include simple loops through an array.
- **Quadratic (O(n^2))**: Algorithms with quadratic time complexity become inefficient for large inputs. Examples include bubble sort and insertion sort.
- **Exponential (O(2^n))**: Algorithms with exponential time complexity are impractical for large inputs due to their rapid growth. Examples include certain recursive algorithms.


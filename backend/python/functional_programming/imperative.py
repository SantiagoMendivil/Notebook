""" 
    Author: Santiago Mendivil
    
    Date: 2025-02-09
    
    Description: 
        This script generates a list of random numbers and
        calculates the mean, median, mode and sorted list
        of the generated list.
"""

import random

def generate_list() -> list:
    """Method that generates a list of 10 random numbers 

    Returns:
        list: List with 10 random numbers
    """
    return [random.randint(1, 100) for i in range(10)]

def median(lst: list) -> float:
    """Method that calculates the median of a list

    Args:
        lst (int): list of integers previously generated

    Returns:
        float: number representing the median of the list
    """
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2-1] + lst[n//2]) / 2
    else:
        return lst[n//2]
def sorted_list(lst: list) -> list:
    """Method that sorts a list using the explicit algorithm

    Args:
        lst (int): list of integers previously generated

    Returns:
        list: list of integers sorted in ascending order
    """
    for i in enumerate(lst):
        min_idx = i
        for j in range(i+1, len(lst)):
            min_idx = j if lst[j] < lst[min_idx] else min_idx
        temp = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx] = temp
    return lst

def mean(lst: list) -> float:
    """Method that calculates the mean of a list

    Args:
        lst (int): list of integers previously generated

    Returns:
        float: Returns the mean of the list
    """
    return sum(lst) / len(lst)

def mode(lst: list) -> int:
    """Method that calculates the mode of a list

    Args:
        lst (int): list of integers previously generated

    Returns:
        int: mode of the list
    """
    counts = {}
    max_count = 0
    mode_value = None
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] > max_count:
            max_count = counts[num]
            mode_value = num
    return mode_value


def __main__():
    lst = generate_list()
    print("Basic statistics:")
    print("Unsorted list:", lst)
    opt = int(input("1. Mean\n2. Median\n3. Mode\n4. Sorted list\nOption: "))

    # Instead of using if-elif we get the method quickly from a dictionary
    case = {
        1: mean,
        2: median,
        3: mode,
        4: sorted_list
    }.get(opt, lambda x: "Invalid option")

    result = case(lst)
    print(result)
__main__()

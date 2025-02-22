def linear_search(search_list: list, target_value):
    """Search for an item in a list using linear search

    Args:
        search_list (list): list of values of x data type
        target_value (_type_): value to find in search_list

    Raises:
        ValueError: target_value not in list

    Returns:
        int: Returns the value of the value found
    """
    matches = []
    for idx in range(len(search_list)):
        if target_value == search_list[idx]:
            matches.append(idx)
    
    if matches:
        return matches 
    else:
        raise ValueError

  
values = [54, 22, 46, 99, 22]
print(linear_search(values, 30))
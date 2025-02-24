def binary_search(sorted_list, target):
    """Binary search using an iterative method
    
    Args:
        :param sorted_list: A list of items
        :param target: The value to search for
        
    Returns:
        :return: The index of the item in the list otherwise "Value not in list 
    """
    left_pointer = 0
    right_pointer = len(sorted_list)
    # fill in the condition for the while loop
    while left_pointer < right_pointer:
        # calculate the middle index using the two pointers
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
        # set the right_pointer to the appropriate value
            right_pointer = mid_idx
        if target > mid_val:
        # set the left_pointer to the appropriate value
            left_pointer = mid_idx + 1
    
    return "Value not in list"
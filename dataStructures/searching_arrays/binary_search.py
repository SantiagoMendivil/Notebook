def binary_search(sorted_list, target):
    """Simple binary search algorithm
    
    Args:
        :param sorted_list: List of sorted items 
        :param target: Item to search for in the list
        
    Returns:
        :return index of the value found, otherwise "value not found
    """
    if not sorted_list:
        return 'value not found'
    mid_idx = len(sorted_list)//2 # Find the mid index
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        left_half = sorted_list[:mid_idx] # select items until mid_idx
        return binary_search(left_half, target)
    if mid_val < target:
        right_half = sorted_list[mid_idx+1:] # select items until mid_idx
        result = binary_search(right_half, target)
        if result == "value not found":
            return result
        else:
            return result + mid_idx + 1
        
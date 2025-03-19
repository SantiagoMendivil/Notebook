"""Migratory birds

    Description:
        Given an array of bird sightings where every element represents a 
        bird type id, determine the id of the most frequently sighted type. 
        If more than 1 type has 
        been spotted that maximum amount, return the smallest of their ids.
        
    Solution proposed first:
        1. Define an empty dictionary that will hold the counts for each bird 
        2. Iterate through the array of types
        3. If the bird type is not in the dictionary, add it with a count of 1
        4. If the bird type is in the dictionaty then adds 1 to the count
        5. Finally returns the max key in the dictionary.
"""


def migratory_birds(arr):
    types = {}
    for it in arr:
        if it not in types:
            types[it] = 1
        else:
            types[it] += 1
    return max(types, key=types.get)


""" 
    Solution proposed second and improved
    
    There is a problem with the code, where if there are multiple birds with the 
    same amount of birds, the code returns the first one to appear, not the minimum
    one. So with the changes it will be like the following solution: 
    
    1. Define an empty dictionary
    2. Iterate through the array of types 
    3. In order to avoid the if else statemes, we use the get method with a default of 
       0, which will add a new key if it does not exist and add 1 to the count
    4. Find the maximum count with max and the values of the dictionary
    5. Return the min key of a bird for each bird and its count in the items if 
       the count is equal to the maximum count.
"""


def migratory_birds_corrected(arr):
    bird_counts = {}
    for bird in arr:
        bird_counts[bird] = bird_counts.get(bird, 0) + 1
    max_count = max(bird_counts.values())
    return min(bird for bird, count in bird_counts.items() if count == max_count)

# If we want to get the minimum value from the array, then just get the min from the
# values of the dictionary.

"""The birthday bar code

    Description: 
        Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

        Lily decides to share a contiguous segment of the bar selected such that:

            The length of the segment matches Ron's birth month, and,
            The sum of the integers on the squares is equal to his birth day.

        Determine how many ways she can divide the chocolate.
        
    Solution Proposed:
        1. Define a method called birthday that receives the following parameters:
            - s: an array of integers, the numbers on each of the squares of chocolate
            - d: an integer, Ron's birth day which represents the sum expected for each sub list
            - m: an integer, Ron's birth month whichs represents the number of elements to use for the sum
        2. Initialize a variable called occurrences and set it to 0 
        3. Check the special condition where, if the length of the list is 1 and if the number in that list 
           is equal to the sum, and also the number of elements to check is 1, then it just returns 1. This 
           because the number already achieves the purpose. 
        4. Loop through the list of elements using the range with the length of the list, substracting
           the number of elements to check the sum and adding 1. len(s) - m checks the last index to start
           without going out of bounds. The +1 is to include the last element in the list. 
        5. Get the segment to compare which is going to be determined as the slicing of the s list from i
        to i + m, which is the number of elements to check the sum for.
        6. Check if the sum of the segment is equal to the sum that we are looking for and add 1 to the occurences
        7. Return the occurences
        
    Notes to consider: 
        - Comparing an element to the next "m" elements without causing an index error:
            - Checking with len(s) - m + 1 is useful for this
        - Slicing from one element into "m" elements
            - arr[i:i+m] 
"""


def birthday(s, d, m):
    occurences = 0
    if len(s) == 1 and s[0] == d and m == 1:
        return 1
    for i in range(len(s) - m + 1):
        segment = s[i:i+1]
        if sum(segment) == d:
            occurences += 1
    return occurences

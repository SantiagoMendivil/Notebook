"""Sock merchant

    Description: 
        There is a large pile of socks that must be paired by color. Given an array of 
        integers representing the color of each sock, determine how many pairs of socks 
        with matching colors there are.
        
    Solution proposed:
        Due we were looking for pairs, instead of looping through the array and 
        looking if the current element meets another element in the item, I voted 
        for counting each of the types, and getting the pairs by dividing the count
        by 2 with // in order to get only integers. And then summ all the pairs for 
        each type. 
        
        1. Declare a dictionary comprehension for array.count(item) // 2 assigned to the
           item for each item in the array. 
        2. returns the sum of the values of the dictionary. 
"""


def sock_merchant(n, ar):
    each_sock = {item: ar.count(item) // 2 for item in ar}
    return sum(each_sock.values())

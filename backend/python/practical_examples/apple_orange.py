""" 
    If we try to read tons of data and check a condition we can use 
        from_range <= condition <= to_range
    This will help in not only readability but also performance.
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_landed = sum(1 for apple in apples if s <= a + apple <= t)
    oranges_landed = sum(1 for orange in oranges if s <= b + orange <= t)

    print(apples_landed)
    print(oranges_landed)

"""drawing book

    Description: 
        A teacher asks the class to open their books to a page number. 
        A student can either start turning pages from the front of the book or 
        from the back of the book. They always turn pages one at a time. 
        When they open the book, pageis always on the right side:
    When they flip page 1 they see pages and 2 and 3 Each page except the last page 
    will always be printed on both sides. The last page may only be printed on the 
    front, given the length of the book. If the book is n pages long, and a student 
    wants to turn to page n, what is the minimum number of pages to turn? They can 
    start at the beginning or the end of the book.
    Given n and p, find and print the minimum number of pages that must be turned in 
    order to arrive at page . 
    
    Solution proposed:
        Since the book has always two pages per sheet, we can calculate how many 
        pages we need to turn from the front and from the back by dividing by 2.
        
        1. From start would be the integer division of the page to find by 2 
        2. From end would be the integer division of the number of pages by 2 minus
           the integer division of the page to find by 2.
        3. Return the minimum between the two values.
"""


def page_count(n, p):
    from_start = p // 2
    from_end = n // 2 - p // 2
    return min(from_start, from_end)

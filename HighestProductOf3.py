"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""

# Brute Force  sort through all the numbers, take 3, and pop the rest

# Solution 1: Brute force
def highest_product(arr):
    """Returns the highest product

    >>> highest_product([1, 2, 3, 4, 5])
    60

    """

    product = 1

    for i in range(3):
        # find the max value in the list, get the index, pop it, and mulitply
        product *= arr.pop(arr.index(max(arr)))

    return product

# Analysis:
# Runtime is O(3n) --> O(n). I bet we can do better...
# Space is constant



d = 1,2,3,4,5

hp3_1(d)

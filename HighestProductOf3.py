"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""

# Solution 1: Brute force,  sort through all the numbers, take 3, and pop the rest
"""
Returns the highest product
    >>> hp3_1([2,4,5,1,3)
    60
"""
def hp3_1(arr):  # highest product of 3 method 1
    arr = sorted(arr)
    arr = arr[:1:-1]    # [start:stop:step]
    product = 1
    for index in arr:
        product *= index
    return product



# Analysis:
# Runtime is O(3n) --> O(n). butt we can do better...
# Space is constant



d = 2,4,5,1,3

ans = hp3_1(d)
print(ans)  # 60



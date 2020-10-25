"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""

# Solution 1: Brute force,  sort through all the numbers, take 3, and pop the rest
"""
1. Sort 
2. Array slice the last 3 indicies 
3. product of 3 indicies in the array
"""


def hp3_1(arr):  # highest product of 3 method 1
    arr = sorted(arr)
    arr = arr[:1:-1]    # [start:stop:step]
    product = 1
    for index in arr:
        product *= index
    return product


# Solution 2: Using a Python one-liner
"""
Lets breakdown that one-liner from inside out
1. find the maximum integer in the array
2. locate the index of that integer in the array
3. pop that index from the array & multiply it to the variable product

arr.pop(arr.index(max(arr))) simply returns a single integer!
"""


def hp3_2(arr):
    product = 1
    for i in range(3):
        product *= arr.pop(arr.index(max(arr)))
    return product


# Analysis:
# Runtime is O(3n) ----> O(n)
# Space is constant O(1)



d = [2,4,5,1,3]

ans = hp3_2(d)
print(ans)  # 60



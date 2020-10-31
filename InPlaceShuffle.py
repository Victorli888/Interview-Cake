"""
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in
each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
"""

# Solution 1: Naive Solution  Walk through the list and swap each element randomly with another.
import random


def swap(x, y):
    temp = y
    y = x
    x = temp


def get_rando(floor, ceiling):
    return random.randrange(floor, ceiling+1)


def naive_shuffle(arr):
    for index_1 in range(0, len(arr)-1):
        # Randomly grab next index
        index_2 = get_rando(0, len(arr)-1)
        # Swap
        if index_2 != index_1:
            arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
    return arr

# This solution is naive because this method doesn't return a uniform solution

test = [1,2,3,4,5,6,7,8,9]
print(f"We want to shuffle: {test}")
ans = naive_shuffle(test)
print(f"Our array now looks like: {ans}")

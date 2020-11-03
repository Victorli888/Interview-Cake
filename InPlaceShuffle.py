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
# Take for example arr = [A,B,C] we allow 3 indices to swap from 3 choices for 3 calls (3*3*3=27)
# However, there are only 6 possible outcomes for how to arrange [A,B,C] (3!=3*2*1)
# 27 is not evenly divisible 6, so our 6 outcomes will be possible with more sets of choices than others.

# Using the same get_rando() function we generate a better method to shuffling in-place
def better_shuffle(arr):
    # If it's 1 or 0 items just return
    if len(arr) <= 1:
        return arr

    last_index = len(arr)-1

    # navigate through from beginning to end
    for curr_index in range(0, len(arr)-1):
        # choose a random index
        random_index = get_rando(curr_index, last_index)

        # Place that random index in the spot we are swapping
        if random_index != curr_index:
            arr[curr_index], arr[random_index] = arr[random_index], arr[curr_index]

# This algorthim is derieved from Fisher-Yates shuffle
# Analysis: Time Complexity: O(n) Space Complexity: O(1)

sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
better_shuffle(sample_list)
print(sample_list)


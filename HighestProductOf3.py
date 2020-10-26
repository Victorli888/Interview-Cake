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

# Analysis sorted() best case is O(n) average case is O(nlogn) we take the best case in BIG O Analysis

# Solution 2: Using a Python one-liner [ONLY POSITIVE NUMBERS]


"""
Lets breakdown that one-liner from inside out
1. find the maximum integer in the array
2. locate the index of that integer in the array
3. pop that index from the array & multiply it to the variable product

arr.pop(arr.index(max(arr))) simply returns a single integer!
"""


def hp3_2(arr):  # Highest Product of 3 Method 2
    product = 1
    for i in range(3):
        product *= arr.pop(arr.index(max(arr)))
    return product


# Analysis:
# Runtime is O(3n) ----> O(n)
# Space is constant O(1)

# Solution 3: Including Negative Integers
"""
1. Sort
2. Initialize an array with 3 indicies -- Space Time O(3) --> O(1)
3. Check whether or not to include negative values
"""


def hp3_3(arr):
    # create a check for long enough list
    if len(arr) < 3:
        raise ValueError("Less than 3 Integers in list")

    arr = sorted(arr)  # step 1

    # For arrays with only positive integers this would be the largest product
    product = arr[-1] * arr[-2] * arr[-3]  # step 2

    # Only 2 neg integers make a positive and the first two integers will generate the largest positive
    largest_positive_pair = arr[-3] * arr[-2]
    largest_negative_pair = arr[0] * arr[1]
    if largest_negative_pair > largest_positive_pair:  # step 3
        product = arr[-1] * arr[0] * arr[1]

    # If all the values are negative then the product will always be negative, so we take the smallest integers possible
    if product < 0:
        product = arr[1] * arr[2] * arr[3]

    return product


# Tests
import unittest
class Test(unittest.TestCase):

    def test_short_list(self):
        actual = hp3_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = hp3_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = hp3_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = hp3_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = hp3_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            hp3_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            hp3_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            hp3_3([1, 1])


unittest.main(verbosity=2)



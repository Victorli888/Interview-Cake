"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:
  [1, 7, 3, 4]

your function would return:
  [84, 12, 28, 21]

by calculating:
  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""


# Brute force method
def get_products_1(arr):  # given array
    #  initialize an array to store values
    output_arr = [1] * len(arr)

    # Loop over indices
    for index in range(len(arr)):

        # Multiply all the integers before index
        for i in arr[:index]:
            output_arr[index] *= i

        # Multiply all the integers after index
        for i in arr[index+1:]:
            output_arr[index] *= i

    return output_arr

# Analysis: Space: O(n)  Time: O(n^2)   --- very no good :/


# Solution 2: keep track of all prior calculations; (memorization)
def get_products_2(arr):

    # Generate arrays for inputs
    products_before_index = [1] * len(arr)
    products_after_index = [1] * len(arr)

    # start at 1 and move forward through the list
    product = 1
    for index in range(len(arr)):
        products_before_index[index] = product
        product *= arr[index]

    # start over for going backward
    product = 1
    for index in range(len(arr)-1, -1, -1):
        products_after_index[index] *= product
        product *= arr[index]


    # Multiply before and after to get output
    output = []

    for index in range(len(arr)):
        output.append(products_before_index[index] * products_after_index[index])

    return output

# Analysis: Time Complexity O(2n) -> O(n)  space complexity: O(2n) -> O(n)

# Solution 3: Testing for Edge Cases
# 1) If only one number? ( you can't find the product of one number) you can but there's no meaning behind it
# 2) Any Zeros? Well, the only number that wouldn't be zero should be that index

def get_products_3(arr):

    # Edge case 1: array that only contains one integer
    if len(arr) < 2:
        raise Exception("Can't Multiply with only one number")

    # Make an array to store products, this will be our output
    output = []

    # Start at product = 1 for the 0th index (This is our running product)
    product = 1
    # loop over indices in the array
    for index in range(len(arr)):
        # append the running product to the output list, starting at 1
        output.append(product)
        # increment the product to include the value at the current integer
        product *= arr[index]

    # Re-initialize the product at 1 to find the products of integers after index
    product = 1
    # Loop backwards over indices to calculate products of integers AFTER
    for index in range(len(arr)-1, -1, -1):
        # First, multiply the current value (all products BEFORE index) by current product of all integers afterward
        output[index] *= product
        # Then, increment product to include the value at current index
        product *= arr[index]

    return output


# Analysis: Time Complexity: O(2n) -> O(n) Space Complexity: O(n)

test = [1,7,3,4]


ans = get_products_3(test)
print(ans)


# Tests
import unittest

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_3([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_3([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_3([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_3([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_3([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_3([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_3([1])


unittest.main(verbosity=2)
"""Write a function which finds an integer that appears more than once in our list.
 (If there are multiple duplicates, you only need to find one of them.)"""

"""
iterative method Iteriate all the way through the array
"""
def fr(arr):  # find repeat
    # Create an array to verify repeated items
    numbers_seen = []
    # iteriate through and find repeats
    for number in arr:
        if number in numbers_seen:
            print("repeat Found!")
            return number

        else: # No repeat found at this step so add it to seen and continue
            numbers_seen.append(number)

    # If the for loop finishes that means no repeats were found in the array
    print("No Repeats found")
    return None

# Analysis Time: O(n) Space: O(n)  ~~~ Worst cases  we can optimize space!

def find_repeat(nums):
    floor = 1
    ceiling = len(nums) -1

    while floor < ceiling:
        mid_pt = floor +((ceiling-floor)//2)
        lower_range_floor, lower_range_ceiling = floor, mid_pt  # Lower Range
        upper_range_floor, upper_range_ceiling = mid_pt+1, ceiling  # Upper Range

    # Count the number of items in the lower range
        items_in_lower_range = 0
        for item in nums:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

            distinct_possible_int_in_lower_range = (lower_range_ceiling - lower_range_floor + 1)
            # Is it in the upper range?
            if items_in_lower_range > distinct_possible_int_in_lower_range:
                # There must be a duplicate in the lower range, approach it iteratively
                floor, ceiling = lower_range_floor, lower_range_ceiling

            else:
                # There must be a duplicate in the upper range, approach it iteratively
                floor, ceiling = upper_range_floor, upper_range_ceiling

    return floor

# Anaylsis Space: O(1) Time: O(nlog(n))


# Tests
import unittest
class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
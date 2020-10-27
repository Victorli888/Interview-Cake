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

# Analysis: O(n)

test = [1,7,3,4]

ans = get_products_1(test)
print(ans)
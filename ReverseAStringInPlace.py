"""
This is Problem 1.2 for the Full Course @ Interview Cake.

Objective: Write a method that takes an array of characters and reverses the letters in place.

"""


def reverse1(arr):

    # Create Pointers
    start = 0
    end = len(arr) - 1

    # Begin swapping
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        # Increment and decrement pointers
        start += 1
        end -= 1

    return arr


def reverse2(arr):
    # initialize pointers
    left = 0
    right = len(arr) - 1

    # begin swapping
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

    # Increment & decrement your pointers
        left += 1
        right -= 1

    return arr


list1 = [1, 2, 3, 4, 5, 6]

print(f"Method 1: {reverse1(list1)} \nNow lets reverse it back!")
# Since we already reversed once
print(f"Method 2: {reverse2(list1)}")  # this would Reverse it back to its original answer

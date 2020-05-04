def fib(number):
    if number < 0:
        raise IndexError(
            'Index was negative'
            'No such thing as a negative index in a series'

        )
    elif number in [0,1]:
        # These are the base cases
        return number

    print(f"Computing fib(%i)" % number)
    return fib(number - 1) + fib(number - 2)

fib(5)
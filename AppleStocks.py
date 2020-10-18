"""Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am
local time. The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock
yesterday.

No "shorting" - you must buy before you sell. You may not buy and sell in the
same time step (at least 1 minute must pass).

"""

# Solution 1: Brute force - try every combination, keep track of max

"""Returns the maximum profit
    >>> get_max_profit_1([10, 7, 5, 8, 11, 9])
    6
"""


def get_max_profit_1(prices):
    # assign a max profit variable to
    max_profit = 0

    # iterate through list of prices, keep track of index, too
    for idx, buy_price in enumerate(prices):
        # calculate profits for prices after current price
        for sell_price in prices[idx+1:]:
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Analysis:
# Runtime O(n) to run through buy_prices, and O(n-1) for sell prices.
# Still O(n^2) for nested loop.


# Solution 2:
def get_max_profit_2(prices):
    """Returns the maximum profit

    >>> get_max_profit_3([10, 7, 5, 8, 11, 9])
    6

    """
    # instantiate variables to track min price, max profit
    min_price = prices[0]
    max_profit = 0

    # iterate over list ONCE
    for price in prices:
        # make sure we're buying at the lowest price we've seen so far
        if price < min_price:
            min_price = price
        # or: min_price = min(min_price, price)
        # calculate potential profit from current price
        profit = price - min_price
        # keep track of profit
        if profit > max_profit:
            max_profit = profit
        # or: max_profit = max(max_profit, profit)

    return max_profit

# Analysis:
# Runtime is O(n) b/c we go through the list only once.







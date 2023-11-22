#!/usr/bin/python3
""" Making Change
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make change for
    a given total.

    Parameters:
        coins (List[int]): A list of coin denominations.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed to make change for the
          given total. Returns -1 if change cannot be made.
    """
    if total <= 0:
        return 0

    if coins is None or not coins:
        return -1

    # Sort coins in descending order
    # it makes more sense to take the largest coins first
    # and reduce the total as much as possible
    coins.sort(reverse=True)

    # Use a greedy approach to pick the largest coins first
    count = 0
    for coin in coins:
        # Reduce the total by the current coin
        # we know at first iteration that the first coin will be the largest
        # this operation should be done as long as total is greater than
        # the current largest coin in the list
        while total >= coin:
            total -= coin
            count += 1

    # If total is reduced to 0, return the count
    if total == 0:
        return count
    else:
        return -1

    # Initialize a list to store the minimum number of coins
    # needed for each amount
    # total has been decresed to some value greater than 0
    # we create an array of size total + 1 and load it with
    # [inf, inf, inf, inf, ...]
    # assingn it to dp - dynamic programming
    # dp = [float("inf")] * (total + 1)

    # # Base case: 0 coins needed to make change for 0
    # dp[0] = 0

    # # Iterate through each coin and update the minimum number of coins needed
    # for coin in coins:
    #     for amount in range(coin, total + 1):
    #         dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # # If dp[total] is still set to infinity, it means the total cannot be met
    # return dp[total] if dp[total] != float("inf") else -1

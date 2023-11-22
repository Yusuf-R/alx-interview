#!/usr/bin/python3
""" Making Change
"""

def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make change for
    a given total using memoization.

    Parameters:
        coins (List[int]): A list of coin denominations.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed to make change for the
          given total. Returns -1 if change cannot be made.
    """
    memo = {}

    def helper(amount):
        """
        Helper function for recursive memoized approach.

        Parameters:
            amount (int): The current amount for which change is being calculated.

        Returns:
            int: The minimum number of coins needed to make change for the
              given amount.
        """
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, 1 + helper(amount - coin))

        memo[amount] = min_coins
        return min_coins

    result = helper(total)

    return result if result != float('inf') else -1


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

    # Initialize a list to store the minimum number of coins
    #  needed for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate through each coin and update the minimum number of coins needed
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still set to infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1

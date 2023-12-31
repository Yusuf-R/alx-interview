#!/usr/bin/python3
""" Prime Game """


# helper function
def check_prime(n):
    # sourcery skip: assign-if-exp, invert-any-all, reintroduce-else, use-any # noqa: E800
    """
    Checks if a number is prime.
    Args:
        n (int): The number to check for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    # Check if n is divisible by any number from 2 to the square root of n.
    # If it is, then n is not prime.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game(number_set):
    """Plays a game of Prime Game.
    Args:
        number_set (int{set} ): The set of numbers to play the game with.
    Returns:
        str: The winner of the game ('Maria' or 'Ben').
    """
    while number_set:
        # Maria will be the first to play
        maria_choice = None

        # Check if a number in the set is prime
        for num in sorted(number_set):
            if check_prime(num):
                maria_choice = num
                break

        # If no prime number is found, Ben starts the next round
        if maria_choice is None:
            return "Ben"
        # if that's not the case, thus maria has gotten a prime number
        # Remove the chosen number and its multiples from the set
        number_set -= set(range(maria_choice, max(number_set) + 1, maria_choice))  # noqa: E501

        # Check if no prime number is left in the updated set,
        # Maria wins the round
        if not any(check_prime(num) for num in number_set):
            return "Maria"

        # Ben plays
        ben_choice = None

        # Check if a prime number is left in the set
        for num in sorted(number_set):
            if check_prime(num):
                ben_choice = num
                break

        # If no prime number is found, Maria starts the next round
        if ben_choice is None:
            return "Maria"

        # Remove Ben's choice and its multiples from the set
        number_set -= set(range(ben_choice, max(number_set) + 1, ben_choice))


def isWinner(x, nums):
    """
    Determines the winner of a game based on the number of rounds and a list of numbers.

    Args:
        x (int): The number of rounds.
        nums (list): A list of numbers.

    Returns:
        The name of the player that won the most rounds. If the winner cannot be determined, return None. # noqa: E501
    """
    # A dictionary to store the counts of wins for each player
    score_board = {'Maria': 0, 'Ben': 0}

    # Check if x is less than 1 or nums is None or empty
    if x < 1 or nums is None or len(nums) == 0:  # noqa: E501
        return None

    # check if all the element in the nums are integers
    if not all(isinstance(n, int) for n in nums):
        return None

    # check if x or nums is greater than 10000
    if x > 10000 or len(nums) > 10000:
        return None

    for n in nums:
        # Play the game and determine the winner for each round
        if n < 1:
            continue
        numbers_set = set(range(1, n + 1))
        winner = play_game(numbers_set)
        # Check if the winner is None (no winner for this round)
        if winner is not None:
            score_board[winner] += 1
        else:
            continue

    # Determine the overall winner
    if score_board['Ben'] > score_board['Maria']:
        return "Ben"
    elif score_board['Maria'] > score_board['Ben']:
        return "Maria"
    else:
        return None

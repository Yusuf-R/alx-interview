#!/usr/bin/python3
""" Prime Game """


def is_prime(n, primes):  # sourcery skip: square-identity
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.
        primes (dict): A dictionary to store previously checked numbers and their primality.  # noqa

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Check for numbers less than 2
    if n < 2:
        return False

    # Check for numbers 2 and 3
    if n < 4:
        return True

    # Check for divisibility by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check if the number has been previously checked
    if n in primes:
        return primes[n]

    # Check for divisibility by numbers greater than 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            primes[n] = False
            return False
        i += w
        w = 6 - w

    # If the number is prime, update the primes dictionary
    primes[n] = True
    return True


def play_game(number_set, primes):
    """
    Play a game based on a set of numbers and a list of prime numbers.

    Args:
        number_set (set): A set of numbers.
        primes (list): A list of prime numbers.

    Returns:
        str: The winner of the game.
    """
    while number_set:
        # Maria's turn
        maria_choice = next(
            (num for num in number_set if is_prime(num, primes)), None)

        if maria_choice is None:
            return "Ben"

        number_set -= set(range(maria_choice,
                          max(number_set) + 1, maria_choice))

        if not any(is_prime(num, primes) for num in number_set):
            return "Maria"

        # Ben's turn
        ben_choice = next(
            (num for num in number_set if is_prime(num, primes)), None)

        if ben_choice is None:
            return "Maria"

        number_set -= set(range(ben_choice, max(number_set) + 1, ben_choice))


def isWinner(x, nums):
    """
    Determine the winner of a game based on a set of numbers.

    Args:
        x (int): The minimum value for the numbers set.
        nums (list): A list of integers representing the numbers set.

    Returns:
        str or None: The name of the winner ('Ben' or 'Maria') or None if there is no winner.  # noqa

    Raises:
        TypeError: If nums is not a list or contains non-integer values.
        ValueError: If x or the length of nums is greater than 10000.

    """

    # Initialize the score board
    score_board = {'Maria': 0, 'Ben': 0}

    # Check for invalid input conditions
    if x < 1 or nums is None or len(nums) == 0:
        return None

    if not all(isinstance(n, int) for n in nums):
        raise TypeError("nums must be a list of integers")

    if x > 10000 or len(nums) > 10000:
        raise ValueError(
            "x and the length of nums must be less than or equal to 10000")

    # Initialize the primes set
    primes = {2: True, 3: True}

    # Iterate over the numbers set
    for n in nums:
        if n < 1:
            continue

        # Generate the numbers set based on the current number
        numbers_set = set(range(2, n + 1, 2)) if n > 2 else {2}

        # Play the game and determine the winner
        winner = play_game(numbers_set, primes)

        # Update the score board
        if winner is not None:
            score_board[winner] += 1

    # Determine the overall winner
    if score_board['Ben'] > score_board['Maria']:
        return "Ben"
    elif score_board['Maria'] > score_board['Ben']:
        return "Maria"
    else:
        return None

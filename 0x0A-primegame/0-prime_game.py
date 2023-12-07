#!/usr/bin/python3
""" Prime Game """


# helper function
def check_prime(n):
    # sourcery skip: assign-if-exp, invert-any-all, reintroduce-else, use-any
    """
    Checks if a number is prime.
    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game(n):
    """ Plays a game of Prime Game.

    Args:
        n (int): The number of rounds to play.

    """
    # we create a set of numbers from n for which we will check if they are prime # noqa: E501
    number_set = set(range(1, n + 1))  # if n = 5, number_set = {1, 2, 3, 4, 5} # noqa: E501
    while number_set:
        # Maria will be first to play
        maria_choice = None
        # we check if number in the set is prime
        for num in number_set:
            if check_prime(num):
                maria_choice = num
                break
        # check if at the end of this set no prime number is found
        # we hand over to Ben
        if maria_choice is None:
            return "Ben"
        # else
        # we remove this number and its multiples from the set
        # like set arithemtic operation (a union b) and  (a intersection b) # noqa: E501
        number_set -= set(range(maria_choice, n + 1, maria_choice))
        # we check if no prime number is left in the updated set, if so
        # Maria wins the round
        flag = 0
        for num in number_set:
            if check_prime(num):
                flag = 1
                break
        if flag == 0:
            # maria wins this round as no prime number is left
            return "Maria"
        # at this stage, we some number is left in the set for the next round # noqa: E501
        # Ben plays
        ben_choice = None
        for num in number_set:
            if check_prime(num):
                ben_choice = num
                break
        # check if at the end of this set no prime number is found
        # we hand over to Maria
        if ben_choice is None:
            return "Maria"
        # we remove Ben choice and it's multiples from the set
        number_set -= set(range(ben_choice, n + 1, ben_choice))


def isWinner(x, nums):
    """ Determines if a player can win the game
    Args:
        x: number of rounds
        nums: list of numbers
        n and x will not be larger than 10000
    Returns:
        The name of the player that won the most rounds
        If the winner cannot be determined,
            return None
    """
    # You can assume n and x will not be larger than 10000
    if x > 10000:
        return None
    if len(nums) > 10000:
        return None
    # a dictionary to store counts
    score_board = {'Maria': 0, 'Ben': 0}

    # Check if x is less than 1 or nums is None or empty
    if x < 1 or nums is None or len(nums) == 0:
        return None

    # playing the game by calling the helper function
    # game is played for x rounds
    # Maria plays first
    # Play each round and update the score_board
    for i in nums:
        winner = play_game(i)
        score_board[winner] += 1

    # Determine the overall winner
    if score_board['Ben'] > score_board['Maria']:
        return "Ben"
    elif score_board['Maria'] > score_board['Ben']:
        return "Maria"
    else:
        return None  # No winner can be determined

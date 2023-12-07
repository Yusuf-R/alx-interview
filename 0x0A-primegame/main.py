#!/usr/bin/python3

# sourcery skip: use-fstring-for-formatting
isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
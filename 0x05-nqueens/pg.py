#!/usr/bin/python3

import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append(list(board))
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, N, solutions)

def solve_n_queens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    solve_n_queens_util(board, 0, N, solutions)

    if not solutions:
        print("No solutions exist")
        sys.exit(1)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for sol in solutions:
        print(sol)

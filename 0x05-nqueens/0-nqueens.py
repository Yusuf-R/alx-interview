#!/usr/bin/python3
""" N queens"""

import sys

# sourcery skip: invert-any-all, remove-unit-step-from-range, use-any, use-next


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at position (row, col) on the board.

    Args:
      board (list[list[int]]): The current state of the board.
      row (int): The row to check.
      col (int): The column to check.
      N (int): The size of the board.

    Returns:
      bool: True if it is safe to place a queen at position (row, col),
      False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

# sourcery skip: invert-any-all, remove-unit-step-from-range, use-any, use-next
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N, solutions):
    """
    Recursively solve the N-Queens problem by placing queens
    on a chessboard of size N x N.

    Args:
      board (List[List[int]]): The current state of the chessboard, represented
      as a 2D list of integers.
      col (int): The current column being processed.
      N (int): The size of the chessboard (number of rows and columns).
      solutions (List[List[Tuple[int, int]]]): A list to store the solutions
      found so far.

    Returns:
      bool: True if a solution was found, False otherwise.
    """
    if col >= N:
        solutions.append([[i, board[i].index(1)] for i in range(N)])
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0

    return res


def solve_n_queens(N):
    """
    Solve the N-Queens problem for a board of size N.

    Args:
      N (int): The size of the board.

    Returns:
      list: A list of solutions, where each solution is a list of N tuples
        representing the positions of the queens on the board. Each tuple
        contains two integers (i, j) representing the row and column of the
        queen, respectively.

    Raises:
      SystemExit: If N is less than 4 or no solutions exist.

    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    if not solve_n_queens_util(board, 0, N, solutions):
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

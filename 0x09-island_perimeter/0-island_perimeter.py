#!/usr/bin/python3
"""island_perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described by a grid.

    Args:
        grid (list[list[int]]): A 2D grid representing the island, where 1 represents land and 0 represents water. # noqa: E501

    Returns:
        int: The perimeter of the island.
    """
    # initialize premeter = 0
    # perimeter of a square = 4 * side length === 4 * 1 === 4
    perimeter = 0
    for rows in range(len(grid)):
        for cols in range(len(grid[rows])):
            if grid[rows][cols] == 1:
                perimeter += 4
                # check if the block above is land
                if rows > 0 and grid[rows - 1][cols] == 1:
                    perimeter -= 2  # subtract 2 because they share the same edge as the block above # noqa: E501
                # check if the block before is land
                if cols > 0 and grid[rows][cols - 1] == 1:
                    perimeter -= 2  # subtract 2 because they share the same edge as the block before # noqa: E501
    return perimeter

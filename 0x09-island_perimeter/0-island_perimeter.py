#!/usr/bin/python3
""" 0-island_perimeter
"""


def island_perimeter(grid):
    """ Input is a two dimensional grid of
        intgers.
        0s represent water
        1 represent land
        Aim is to find the perimeter where land bordered by water.
    """
    len_row = len(grid)
    len_col = len(grid[0])

    connections = 0
    perimeter = 0

    for i in range(0, len_row):
        for j in range(0, len_col):

            if grid[i][j] == 1:
                perimeter += 4

                if i != 0 and grid[i - 1][j] == 1:
                    connections += 1

                if j != 0 and grid[i][j - 1] == 1:
                    connections += 1

    boundaries = perimeter - (connections * 2)

    return boundaries

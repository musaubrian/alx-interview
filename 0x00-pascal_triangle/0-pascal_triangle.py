#!/usr/bin/python3
"""Function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """return pascal's triangle

    Args::
        n(int): the starting point of the triangle
    """

    triangle = []
    if n <= 0:
        return triangle

    triangle.append([1])
    for i in range(n - 1):
        triangle.append([1] + [triangle[i][j] + triangle[i][j + 1]
                               for j in range(len(triangle[i]) - 1)] + [1])
    return triangle

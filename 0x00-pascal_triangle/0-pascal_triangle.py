#!/usr/bin/env python3
"""
return a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    return pascal's triangle

Args::
    n(int): the starting point of the triangle
    """

    triangle = []

    if n <= 0:
        return triangle
    else:
        for i in range(n):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)
        return triangle

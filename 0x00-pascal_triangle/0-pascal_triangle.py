#!/usr/bin/python3
"""A script to  determine the pascal triangle of a number"""


def pascal_triangle(n):
    """
    returns a list of lists of .integers representing the pascal's triangle of n
    """
    triangle = []

    # returns (triangle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    return triangle

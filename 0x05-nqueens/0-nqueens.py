#!/usr/bin/python3
"""A program to solve the N Queens puzzle on an NxN chessboard"""


import sys


def find_solutions(row, column):
    """Recursively generates all possible N Queens solutions"""
    result = [[]]
    for queen in range(row):
        result = place_queen(queen, column, result)
    return result


def place_queen(queen, column, previous_result):
    """Places a queen on the next column and returns all safe positions"""
    safe_positions = []
    for solution in previous_result:
        for x in range(column):
            if is_safe(queen, x, solution):
                safe_positions.append(solution + [x])
    return safe_positions


def is_safe(q, x, solution):
    """Checks if a queen can be safely placed at the given position"""
    if x in solution:
        return False
    else:
        return all(abs(solution[column] - x) != q - column
                   for column in range(q))


def initialize():
    """Parses the command-line argument and checks its validity"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def solve_n_queens():
    """Solves the N Queens problem and prints all solutions"""
    n = initialize()
    solutions = find_solutions(n, n)
    for solution in solutions:
        cleaned_solution = []
        for row, column in enumerate(solution):
            cleaned_solution.append([row, column])
        print(cleaned_solution)


if __name__ == '__main__':
    solve_n_queens()


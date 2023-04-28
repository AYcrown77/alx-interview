#!/usr/bin/env python3
"""
Module for the N queens puzzle
"""

import sys


def main():
    """
    Function that implements all possible solutions to
    the n queens problem
    """
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    board = {}
    for i in range(1, n + 1):
        board[i] = alph[i - 1]

    return []

if __name__ == '__main__':
    main()

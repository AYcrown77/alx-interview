#!/usr/bin/env python3
"""
The N queens puzzle is the challenge of placing 
N non-attacking queens on an N×N chessboard.
"""

import sys


def main():
    """
    implements all possible solutions to
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

    aux = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    board = {}
    for i in range(1, n + 1):
        board[i] = aux[i - 1]

    return []

if __name__ == '__main__':
    main()

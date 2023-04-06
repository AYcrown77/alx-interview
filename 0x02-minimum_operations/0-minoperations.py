#!/usr/bin/python3
"""Performs minimum operations"""


def prime_factor(n):
    """Returns the prime factors of a given number"""
    factor = []
    for i in range(2, n // 2):
        while (n % i == 0):
            factor.append(i)
            n = n / i
        if (i >= n):
            break
    if n > 1:
        factor.append(n)
    return factor


def minOperations(n):
    if (n <= 1):
        return 0

    factors = prime_factor(n)

    add = 0
    for i in factors:
        add += i
    return add

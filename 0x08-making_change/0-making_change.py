#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a
    given amount total.
    """
    num = 0
    coins.sort(reverse=True)
    if total < 0:
        return 0
    for coin in coins:
        if total % coin <= total:
            num += total // coin
            total = total % coin

    return num if total == 0 else -1

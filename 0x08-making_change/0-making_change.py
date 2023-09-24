#!/usr/bin/python3
'''making_change'''


def makeChange(coins, total):
    """ This is an alx interview challenge
        Args:
        -coins
        -total
        Calculates the minimum amount of coins required to make change
    """
    coins = sorted(coins, reverse=True)
    count = 0

    if total <= 0:
        return 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total == 0:
        return count
    return -1

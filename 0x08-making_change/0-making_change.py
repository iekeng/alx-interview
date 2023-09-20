#!/usr/bin/python3
'''making_change'''


def makeChange(coins, total):
    """ This is an alx interview challenge
        Args:
        -coins
        -total
        Calculates the minimum amount of coins required to make change
    """
    coins.sort()
    amount = 0

    if total <= 0:
        return 0

    while total > 0 and coins:
        highest = coins[-1]

        if highest <= total:
            num_coins = total // highest
            amount += num_coins
            total -= num_coins * highest
        else:
            coins.pop()
            if coins[-1] > total:
                return -1

    return amount

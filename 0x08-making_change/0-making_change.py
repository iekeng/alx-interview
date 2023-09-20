#!/usr/bin/python3
'''making_change'''


def makeChange(coins, total):
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

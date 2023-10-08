#!/usr/bin/python3
""" Prime Game
"""


def prime_num(start, end):
    """ Select and return prime numbers from
        the list of consecutive numbers between
        1 and number
    """
    prime_nums = []

    for num in range(start, end + 1):

        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False

        if is_prime:
            prime_nums.append(num)

    return prime_nums


def isWinner(x, nums):
    """ this function determines the winner of
        the prime game between maria and ben
    """
    maria_score = 0
    ben_score = 0

    if not x or not nums:
        return None

    for rounds in range(x):
        result = prime_num(1, nums[rounds])
        if len(result) % 2 == 0:
            maria_score += 1
        else:
            ben_score += 1
    if maria_score > ben_score:
        return 'Maria'
    else:
        return 'Ben'

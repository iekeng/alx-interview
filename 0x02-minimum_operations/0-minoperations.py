#!/usr/bin/env python3
'''Finding minimum operations for copy all and paste operations'''


def minOperations(n):
    '''given n number of items'''
    if n <= 0:
        return 0
    elif n % 3 == 0:
        res = n // 3
        return 3 + res
    elif n % 2 == 0:
        if n == 2:
            return n
        elif n == 4:
            return n
        else:
            return (2 + (n / 2))
    else:
        return n

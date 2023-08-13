#!/usr/bin/python3
'''Finding minimum operations for copy all and paste operations'''


def minOperations(n: int) -> int:
    '''given n number of items'''
    divisor: int = 2
    operations: int = 0

    if (n <= 1):
        return 0

    while (n > 1):
        while (n % divisor == 0):
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

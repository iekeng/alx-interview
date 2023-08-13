#!/usr/bin/python3
'''Finding minimum operations for copy all and paste operations'''


def minOperations(n):
    '''given n number of items'''
    divisor = 2
    operations = 0

    if n <= 0:
        return 0

    while (n > 1):
        while(n % divisor == 0):
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

    

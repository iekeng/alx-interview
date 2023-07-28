#!/usr/bin/python3
'''
alx interview
'''


def pascal_triangle(n):
    res = [[1]]
    for i in range(n - 1):
        row = []
        temp = [0] + res[-1] + [0]
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res
#!/usr/bin/python3
'''0-validate_utf8'''


def validUTF8(data):
    '''validates data'''
    try:
        bytes(data)
        return True
    except ValueError:
        return False

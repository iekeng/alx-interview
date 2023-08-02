#!/usr/bin/python3
'''Lockboxes solution'''


def canUnlockAll(boxes):
    '''appends numbers in individual arrays to a new keys array
       without any being repeated and then compares the length of the
       keys array to the boxes array.
    '''
    key = []
    for item in boxes:
        if not item:
            return False
        else:
            for val in item:
                if val not in key:
                    key.append(val)
        if len(key) == len(boxes) - 1:
            return True

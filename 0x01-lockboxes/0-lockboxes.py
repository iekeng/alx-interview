#!/usr/bin/python3
'''Lockboxes solution'''
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# boxes = [[1], [2], [3], [4], []]
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

def canUnlockAll(boxes):
    '''appends numbers in individual arrays to a new keys array
        without any being repeated and then compares the length of the
        keys array to the boxes array.
    '''

    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box (index 0) as opened
    keys_to_check = boxes[0]

    while keys_to_check:
        key = keys_to_check.pop()
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys_to_check.extend(boxes[key])

    return len(opened_boxes) == len(boxes)

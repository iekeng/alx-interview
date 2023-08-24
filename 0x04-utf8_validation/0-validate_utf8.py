#!/usr/bin/python3
'''0-validate_utf8'''


def validUTF8(data):
    '''validates data'''
    remaining_bytes = 0

    for byte in data:
        # if remaining_bytes > 0 and (byte & 0b11000000) == 0b10000000:
        #   remaining_bytes -= 1
        if remaining_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:  # 1-byte character
                remaining_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:  # 2-byte character
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:  # 3-byte character
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:  # 4-byte character
                remaining_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Invalid continuation byte
            return False

    return remaining_bytes == 0

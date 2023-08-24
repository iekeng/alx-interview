def validUTF8(data):
    # Variable to keep track of the number of remaining bytes for the current character
    remaining_bytes = 0
    
    for byte in data:
        # Check if this byte is a continuation byte (starts with 10xxxxxx)
        if remaining_bytes > 0 and (byte & 0xC0) == 0x80:
            remaining_bytes -= 1
        elif remaining_bytes == 0:
            # Check how many bytes are used to encode this character
            if (byte & 0x80) == 0:  # 1-byte character
                remaining_bytes = 0
            elif (byte & 0xE0) == 0xC0:  # 2-byte character
                remaining_bytes = 1
            elif (byte & 0xF0) == 0xE0:  # 3-byte character
                remaining_bytes = 2
            elif (byte & 0xF8) == 0xF0:  # 4-byte character
                remaining_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Invalid continuation byte
            return False
    
    # All bytes have been processed and validated
    return remaining_bytes == 0


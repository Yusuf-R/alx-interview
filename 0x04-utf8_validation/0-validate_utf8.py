#!/usr/bin/python3
"""UTF-8 Validation"""


def is_valid_continuation_byte(byte):
    """
    Determines if a given byte represents a valid continuation byte.
    Args:
        byte (int): The byte to check.
    Returns:
        bool: True if the byte is a valid continuation byte, else False.
    """
    # Define masks for the significant bits
    START_BYTE_MASK = 1 << 7  # 10000000 in binary
    SECOND_BIT_MASK = 1 << 6  # 01000000 in binary
    # Check if the leftmost bit is 1 and the second leftmost bit is 0
    if (byte & START_BYTE_MASK) and not (byte & SECOND_BIT_MASK):
        return True
    else:
        return False


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the bytes of
        a UTF-8 encoded character sequence.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    # Ensure data will be represented by a list of integers
    if not isinstance(data, list):
        print("Entry data must be a list of integers")
        return False
    if not all(isinstance(num, int) for num in data):
        print("Entry data must be a list of integers")
        return False

    # Ensure data is a valid UTF-8 encoding
    n_bytes = 0

    # loop thorough each data
    for num in data:
        if n_bytes == 0:
            # set a mask bit of 128
            mask = 1 << 7
            # determine the number of bytes to repr character
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            # if after the loop n_bytes == 0
            if n_bytes == 0:
                # continue with the next data in the list
                continue
            # Important Note:
            # a valid utf will have n_bytes to be 0,2,3,or 4
            # 1 and > 4 are not valid
            # check if n_bytes == 1 or > 4
            elif n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # at this stage, the n_bytes is either
            # 2,3,or 4
            # thus we have something called a continuation bytes
            # they represent [10xxxxx] for muli-byte sequences
            if not is_valid_continuation_byte(num):
                return False
        n_bytes -= 1
    return n_bytes == 0

#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the bytes of
        a UTF-8 encoded character sequence.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """

    bytes_to_follow = 0

    for num in data:
        bin_rep = format(num, "08b")

        if bytes_to_follow == 0:
            if bin_rep.startswith("0"):
                bytes_to_follow = 0
            elif bin_rep.startswith("110"):
                bytes_to_follow = 1
            elif bin_rep.startswith("1110"):
                bytes_to_follow = 2
            elif bin_rep.startswith("11110"):
                bytes_to_follow = 3
            else:
                return False
        elif bin_rep.startswith("10"):
            bytes_to_follow -= 1

        else:
            return False
    return bytes_to_follow == 0

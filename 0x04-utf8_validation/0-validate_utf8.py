#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.
    """
    byte_no = 0
    msk = 255

    for byte in data:
        if byte_no == 0:
            byte = byte & msk
            if (byte >> 5) == 0b110:
                byte_no = 1
            elif (byte >> 4) == 0b1110:
                byte_no = 2
            elif (byte > 3) == 0b11110:
                byte_no = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            byte_no -= 1

    return byte_no == 0

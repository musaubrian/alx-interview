#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return:
        True if data is a valid UTF-8 encoding, else return False
    """
    new = []
    for num in data:
        n = num & 0xFF
        if num < -256:
            return False
        new.append(n)

    try:
        bytes(new).decode(encoding="utf-8", errors="strict")
    except (ValueError, UnicodeEncodeError):
        return False

    return True

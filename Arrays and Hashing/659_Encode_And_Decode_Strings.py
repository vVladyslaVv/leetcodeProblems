from collections import defaultdict
from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        encoded = ""
        for str in strs:
            encoded += f"{len(str)}${str}"
        return encoded

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        decoded, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "$":
                j += 1
            int_len = int(str[i:j])
            i = j + int_len + 1
            decoded.append(str[j+1:i])
        return decoded

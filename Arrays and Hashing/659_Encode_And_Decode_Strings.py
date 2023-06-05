from collections import defaultdict
from typing import List

# We use $ as an encoding divider and we also specify length of the encoded string that goes after divider
# as and integer before the divider. That way when we decode we just loop threw the encoded string and check for $
# and then use second counter j to specifically find the $ and we convert our number from string to integer.#
# In the end we increment i on j and +1 to go to the next element after the $.
# And there we can finally append our decoded string that is from j+1 to i now. Then j =  i again and we repeat
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

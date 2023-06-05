from typing import List


# First of all we'd check if the length of both strings is similar to validate, if they even can be anagrams.
# Then we can create two hashMaps and use letters as keys and increase value each time letter occurs in a string.
# In the end we simply compare values (number of occurrences) for each key (letters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
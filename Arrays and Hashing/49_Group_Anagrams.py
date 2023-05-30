from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = []
        strsHash = {}
        for str in strs:
            checkedStr = ''.join(sorted(str))
            if checkedStr in strsHash:
                strsHash[checkedStr].append(str)
            else:
                strsHash[checkedStr] = [str]
        for key in strsHash:
            returnList.append(strsHash[key])
        return returnList


# Another Possible Solution
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsHash = defaultdict(list)
        for str in strs:
            count = [0] * 26 # a ..... z

            for c in str:
                count[ord(c) - ord("a")] += 1

            strsHash[tuple(count)].append(str)

        return strsHash.values()
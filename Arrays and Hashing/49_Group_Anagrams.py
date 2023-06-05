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


# Another Possible Solution We'd create a defaultdict hashMap  and a count list with 0 and length of an alphabet.
# Then for each string in list of strings we'd check every character with ASCII code and increment corespondent value
# in our alphabet count list. Then we can transform the list into a tuple of values and actually use it as a key in
# our hashMap. The value will be a list of strings, where we will append a new string each time we have same count of
# letters (anagram) in our alphabet counter list(tuple). In the end we simply return the values of our hashMap (lists
# with strings)
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsHash = defaultdict(list)
        for str in strs:
            count = [0] * 26 # a ..... z

            for c in str:
                count[ord(c) - ord("a")] += 1

            strsHash[tuple(count)].append(str)

        return strsHash.values()
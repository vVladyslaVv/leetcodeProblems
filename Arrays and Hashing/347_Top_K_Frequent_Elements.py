from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        returnList = []
        for i in range(len(nums)):
            hashMap[nums[i]] += 1

        for i in reversed(sorted(hashMap, key=hashMap.get)):
            if k > 0:
                returnList.append(i)
                k -= 1

        return returnList


# Solution with Bucket Sort Variation Let's use bucket sort for this solution. First of all let's create a list of
# lists (number of lists has to be same as number of elements in nums, in case all elements is unique).
# Then we count number of occurrences of every single element in nums and increment value under the correspondent key
# In the end we append values into a bucketSort list on a position, corresponding to a number of occurrences.
# That way, the bigger the index in the array, the bigger number of occurrences we have. After it, we just loop threw
# the list backwards and create a res list with k elements.
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucketSort = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
        for n, c in hashMap.items():
            bucketSort[c].append(n)
        res = []
        for i in range(len(bucketSort) - 1, 0, -1):
            for n in bucketSort[i]:
                res.append(n)
                if len(res) == k:
                    return res

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
                k-= 1

        return returnList

# Solution with Bucket Sort Variation
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucketSort = [[] for i in range(len(nums) + 1 )]

        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
        for n , c in hashMap.items():
            bucketSort[c].append(n)
        res = []
        for i in range(len(bucketSort) - 1, 0, -1):
            for n in bucketSort[i]:
                res.append(n)
                if len(res) == k:
                    return res



from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashNums = {}  # val:index

        for i, n in enumerate(nums):
            if target - n in HashNums:
                return [HashNums[target - n], i]
            HashNums[n] = i


# Possible 2 solution
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

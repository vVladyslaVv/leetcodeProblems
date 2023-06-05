from typing import List


# We'll create a hashMap of processed values when looping threw the list. Then on each step of the loop we'd check if
# we have a second value we need (target - current value) in all previous values If that's not a case, we just create
# a new val:index pair in the hashMap and repeat the checking process for next value
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

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            midway = left + ((right - left) // 2)
            if nums[midway] == target:
                return midway
            elif nums[midway] < target:
                left = midway + 1
            else:
                right = midway - 1

        return -1

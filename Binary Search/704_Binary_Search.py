from typing import List

# We use 2 pointers and divide and conquer algorithms
# As our array is sorted, each time we calculate the midway point
# and compare it to the target, that way we no which pointer we have to shift
# We do it until our midway meats the target
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

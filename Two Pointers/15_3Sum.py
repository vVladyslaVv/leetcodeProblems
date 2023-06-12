from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res

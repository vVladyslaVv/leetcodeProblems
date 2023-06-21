from typing import List

# First of all we will sort our array
# While iterating threw the array we will pass the element if it's the same as previous
# we start with left being i+1 and right as max right
# While slowly going to the middle we check if our triplet (left pnt + right pnt + i)
# As our array is sorted, we just shift left pnt if sum is too low and right if sum is too big
# Else we append our result to the res array and then shift left pnt by one, after what we
# incrementing left while left is same, thus ensuring that it won't write down a lot of duplicates
# to the res array

# We don't need to check elements before i, because if i participates in the 3sum, then
# if would already be used while checking previous elements, thus going before i will
# just create duplicates
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

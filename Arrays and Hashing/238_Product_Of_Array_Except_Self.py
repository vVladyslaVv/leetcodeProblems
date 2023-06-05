from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # strore left product in res
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        right_prod = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]
            res[i] *= right_prod[i]
        return res


# 1 pass solution We create a result list with all 1 and two variables: postfix and prefix. Each of them is
# incremented one by one, so in each step both of them contains products on the left of them or on the right of them.
# Then each element in res is multiplied by prefix and postfix 1 time.
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            res[len(nums)-1-i] *= postfix
            postfix *= nums[len(nums)-1-i]
        return res

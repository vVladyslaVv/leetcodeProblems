from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            while numbers[left] + numbers[right] != target and numbers[left] + numbers[right] > target:
                right -= 1
            while numbers[left] + numbers[right] != target and numbers[left] + numbers[right] < target:
                left += 1

        return [left + 1, right + 1]


# Faster Solution
# Again we create 2 pointers and iterate threw the list until left pointer doesn't exceeds right pointer.
# For each step we use that list is sorted in non decreasing order, so we check value on left and right
# pointer. If sum exceeds target, then we need to move right pointer (because we want smaller value) and
# if sum if lower then target we move left pointer (because now we need bigger value).
# By definition list must have at least one solution, which means we will always get
# values that sums up to the target and we return their indices (+1 by condition)
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            step_sum = numbers[left] + numbers[right]
            if step_sum < target:
                left += 1
            elif step_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

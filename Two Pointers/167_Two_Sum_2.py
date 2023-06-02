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

        return [left+1, right+1]



# Faster Solution
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


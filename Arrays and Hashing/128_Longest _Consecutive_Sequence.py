from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        consecutive_longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                current_length = 0
                while (num + current_length) in numSet:
                    current_length += 1
                if current_length > consecutive_longest:
                    consecutive_longest = current_length

        return consecutive_longest

from typing import List

# First of all we create a hashMap out of nums list. Then for each element we check if it's the start of the
# consecutive elements (if num-1 not in hashMap, then it's start) and then we just increment our local counter until
# we have a consecutive numbers contained in the set. if our local counter is bugger then our global countet, then it's
# new longest consecutive streak
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

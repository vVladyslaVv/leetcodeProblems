from typing import List

# We are using 2 pointers, most left and most right.
# Then we slowly progressing towards the middle, and if left barrier is
# smaller then right one, then we shift left pointer by one, else
# we shift right pointer. On each step we compare the S with maxS
# By always shifting pointer with smaller barrier, we ensure
# that our square can theoretically grow
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        res = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            res = max(res, min(height[left], height[right]) * (right - left))
        return res



from typing import List

# if height array is empty just return 0
# Else we have left and tight pnt
# Then we are always counting left and right max
# If leftMax is smaller then rightMax we shift the left pinter and calculate the new max
# then we are calculating and adding to the existing result how many water can be stored in the current
# height (leftMax - current height) is number of water we can store
# Same works for right pointer
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]

        return res

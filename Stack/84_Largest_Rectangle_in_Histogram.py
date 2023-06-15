from typing import List


# Fast Stack Solution
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxS = 0
        lenH = len(heights)
        stack = []  # index, height pair
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxS = max(maxS, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxS = max(maxS, h * (lenH - i))
        return maxS




# Bruteforce

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i, height in enumerate(heights):
            if i != 0 and i != len(heights) - 1:
                left = i - 1
                right = i + 1
                while left >= 0 and heights[left] >= height:
                    left -= 1
                while right < len(heights) and heights[right] >= height:
                    right += 1
                res = max(res, (right - left - 1) * height)

            elif i == 0:
                right = i + 1
                while right < len(heights) and heights[right] >= height:
                    right += 1
                res = max(res, (right - i) * height)
            else:
                left = i - 1
                while left >= 0 and heights[left] >= height:
                    left -= 1
                res = max(res, (i - left) * height)

        return res

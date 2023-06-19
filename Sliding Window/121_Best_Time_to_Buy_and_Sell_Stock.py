from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxInc = 0
        while right < len(prices):
            currInc = prices[right] - prices[left]
            if currInc < 0:
                left = right
                right += 1
            else:
                maxInc = max(maxInc, currInc)
                right += 1

        return maxInc


# Faster Solution, but more memory
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxInc = 0
        while right < len(prices):
            if prices[right] - prices[left] > 0:
                maxInc = max(maxInc, prices[right] - prices[left])

            else:
                left = right
            right += 1

        return maxInc
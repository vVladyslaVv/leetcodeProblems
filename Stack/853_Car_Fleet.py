from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        PosSpeed = sorted(list(zip(position, speed)))

        res = []
        for p, s in PosSpeed[::-1]:
            res.append((target - p)/s)
            if len(res) >= 2 and res[-2] >= res[-1]:
                res.pop()
        return len(res)
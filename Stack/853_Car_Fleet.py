from typing import List

# First of all we sort our array by positions on the road, creating tuples of position, speed.
# Then we are iterating threw the list from the end
# (so, first we take the car that is the closest to target).
# After that we append the stack with time, for each individual car to finish the road
# In case, time for the car to reach target is same or smaller than the time for the car ahead of it ([-2] in stack)
# we pop the car, because it will catch up with the car ahead of it before reaching the target,
# thus it won't create a new car fleet and we won't count it. In the end we just return length of stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        PosSpeed = sorted(list(zip(position, speed)))

        res = []
        for p, s in PosSpeed[::-1]:
            res.append((target - p)/s)
            if len(res) >= 2 and res[-2] >= res[-1]:
                res.pop()
        return len(res)
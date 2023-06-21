from typing import List

# First of all we create an empty stack an empty result list.
# Then we iterate threw all temperatures and if stack is not empty and current temperature is warmer
# then the temperature under the index, last pushed to the stack, then we can pop the stack and on the
# popped index in the result list we will place current index - popped index (number of days to get warmer)
# While ensures that if temperature is bigger then all temperatures before, it will pop the stack until there
# is no smaller temperature behind
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tmp = stack.pop()
                result[tmp] = (i - tmp)
            stack.append(i)
        return result



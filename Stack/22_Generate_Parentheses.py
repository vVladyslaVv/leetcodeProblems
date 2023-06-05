from typing import List

# Let's use backtracking here. Inside backtracking function we create local variables for opened and closed
# parentheses We basically append to result when opened = closed = n, if not we recursively call backtrack if opened
# < n or closed < opened with parameters like opened + 1 or closed + 1, and then pop to execute the backtracking itself
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(opened, closed):
            if opened == closed == n:
                result.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return result

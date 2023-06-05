
# First of all we create a dictionary where closed Parentheses is keys and opened is values Then we append only opening
# Parentheses to stack, but if it's a closing one, then we check for a previous element of the stack and pop it if
# it's an opening Parentheses. In other case we straightforward return false. In the end if our stack is empty,
# it means that all opening paradises got their matching closing Parentheses and where popped. Else we return false.
class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {")": "(",
                          "]": "[",
                          "}": "{"}
        stack = []
        for char in s:
            if char in parenthesesMap:
                if stack and stack[-1] == parenthesesMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False



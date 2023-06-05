from typing import List

# We jsut check for chars to be +, -, * or / and then take two previous values from stack and do the math operation.
# If it's not mathematical operation we just append stack.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valueStack = []
        a, b, c = 0, 0, 0
        for char in tokens:
            if char == "+":
                b = int(valueStack.pop())
                a = int(valueStack.pop())
                c = a + b
                valueStack.append(c)

            elif char == "-":
                b = int(valueStack.pop())
                a = int(valueStack.pop())
                c = a - b
                valueStack.append(c)


            elif char == "*":
                b = int(valueStack.pop())
                a = int(valueStack.pop())
                c = a * b
                valueStack.append(c)


            elif char == "/":
                b = int(valueStack.pop())
                a = int(valueStack.pop())
                c = a / b
                valueStack.append(c)
            else:
                valueStack.append(char)
        return int(valueStack.pop())

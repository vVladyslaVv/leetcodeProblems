from typing import List


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

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                x, y = stack.pop(), stack.pop()
                stack.append(x + y)
            elif s == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif s == "*":
                x, y = stack.pop(), stack.pop()
                stack.append(x * y)
            elif s == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(s))

        return stack[0]
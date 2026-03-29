class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == "+":
                a, b = stack.pop(), stack.pop()
                val = int(a) + int(b)
                stack.append(val)
            elif num == "-":
                a, b = stack.pop(), stack.pop()
                val = int(b) - int(a)
                stack.append(val)
            elif num == "*":
                a, b = stack.pop(), stack.pop()
                val = int(a) * int(b)
                stack.append(val)
            elif num == "/":
                a, b = stack.pop(), stack.pop()
                val = int(float(b)/int(a))
                stack.append(val)
            else:
                stack.append(num)
        return int(stack[-1])
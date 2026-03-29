class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashmap = {
            "+": lambda x, y: x + y ,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
            }
        stack = []
        for i in tokens:
            if i not in hashmap.keys():
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                res = hashmap[i](int(a),int(b))
                stack.append(res)
        return int(stack[-1])

        #My Algorithm
        # 1. Read tokens left → right.
# ✅ Correct approach.

# 2. Keep a running total.
# ❌ Wrong: RPN does not use a running total; the stack itself maintains state.

# 3. For a number: push it to the stack.
# ✅ Correct: operands should always be pushed until an operator is seen.

# 4. For a symbol/operator:
#    - Pop the top number and combine it with total as total = total (op) popped.
#    ❌ Wrong: you must pop TWO numbers (b then a), compute a op b, and push the result.
#    - If total isn’t initialized, you tried to set it using pops in an ad-hoc way.
#    ❌ Wrong: no ad-hoc rules; the stack always contains the operands you need.

# 5. Division rule you assumed: if result is negative, force it to 0; or use floor division.
# ❌ Wrong: the correct rule is truncate toward zero (int(a / b)), not floor, and never force 0.

        
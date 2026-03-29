class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval = val if not self.minstack else min(val, self.minstack[-1])
        self.minstack.append(self.minval)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
        

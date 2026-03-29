class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval = min(self.minval,val)
        self.minstack.append(self.minval)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
        

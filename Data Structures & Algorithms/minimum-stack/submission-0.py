class MinStack:

    @property
    def stack(self):
        return self._stack

    @property
    def minStack(self):
        return self._minStack

    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

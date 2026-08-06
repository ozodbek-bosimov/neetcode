class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.m or self.m[-1] >= val:
            self.m.append(val)
        return None
    def pop(self) -> None:
        rmv = self.s.pop()
        if self.m and self.m[-1] == rmv:
            self.m.pop()
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
    

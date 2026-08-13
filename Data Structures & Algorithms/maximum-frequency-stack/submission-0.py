class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = {}
    def return_max_frequent_element(self):
        return max(self.count.values())

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] = self.count.get(val, 0) + 1
        return

    def pop(self) -> int:
        mfe = self.return_max_frequent_element()
        n = len(self.stack) - 1
        while n >= 0:
            if  mfe > 0 and self.count.get(self.stack[n], 0) == mfe:
                self.count[self.stack[n]] -= 1
                return self.stack.pop(n)
            n -= 1
        
        return -1



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
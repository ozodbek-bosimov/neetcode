class MyQueue:

    def __init__(self): # pop, append
       self.i = []
       self.o = []

    def push(self, x: int) -> None:
        # ~O(1)
        self.i.append(x)
        return None

    def pop(self) -> int:
        # ~O(1)
        if not self.o:
            while self.i:
                self.o.append(self.i.pop())
        return self.o.pop()

    def peek(self) -> int:
        # ~O(1)
        if not self.o:
            while self.i:
                self.o.append(self.i.pop())
        return self.o[-1]

    def empty(self) -> bool:
        # O(1)
        return len(self.i) + len(self.o) == 0


        

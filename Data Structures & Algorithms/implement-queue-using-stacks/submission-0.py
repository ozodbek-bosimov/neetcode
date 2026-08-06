class MyQueue:

    def __init__(self): # pop, append
       self.i = []
       self.o = []

    def push(self, x: int) -> None:
        self.i.append(x)
        return None

    def pop(self) -> int:
        if not self.o:
            while self.i:
                self.o.append(self.i.pop())
        return self.o.pop()

    def peek(self) -> int:
        if not self.o:
            while self.i:
                self.o.append(self.i.pop())
        return self.o[-1]

    def empty(self) -> bool:
        return len(self.i + self.o) == 0
        

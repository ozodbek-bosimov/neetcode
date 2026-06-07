from collections import deque # only: append, popleft
class MyStack:
    def __init__(self):
        self.q = deque() 

    def push(self, x: int) -> None: 
        # T: O(n)
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return None

    def pop(self) -> int:
        # O(1)
        return self.q.popleft()

    def top(self) -> int:
        # O(1)
        return self.q[0]

    def empty(self) -> bool:
        # O(1)
        return len(self.q) == 0

        
from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque() # (append, popleft) or (appendleft, pop)

    def push(self, x: int) -> None:
        self.queue.append(x)
        n = len(self.queue)
        for _ in range(n - 1):
            self.queue.append(self.queue.popleft())
        return None
    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    
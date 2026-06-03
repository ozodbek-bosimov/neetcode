class Node:
    def __init__(self, val="", next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        # O(1)
        vis = Node(val = url, next = None, prev = self.curr)
        self.curr.next = vis
        self.curr = vis

    def back(self, steps: int) -> str:
        # O(steps)
        for _ in range(steps):
            if self.curr.prev is None:
                return self.curr.val
            self.curr = self.curr.prev
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        # O(steps)
        for _ in range(steps):
            if self.curr.next is None:
                return self.curr.val
            self.curr = self.curr.next
        
        return self.curr.val
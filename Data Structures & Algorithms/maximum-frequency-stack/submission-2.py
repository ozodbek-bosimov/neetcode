from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.count = defaultdict(int) 
        """
        5 : 2
        7: 2
        """
        self.mcnt = 0
        """
        2
        """
        self.buckets = defaultdict(list)
        """
        1: [5, 7]
        2: [5, 7]
        """

    def push(self, val: int) -> None:
        cnt = self.count[val] + 1
        self.count[val] = cnt
        if self.mcnt < cnt:
            self.mcnt = cnt
        self.buckets[cnt].append(val)
        return

    def pop(self) -> int:
        rm = self.buckets[self.mcnt].pop()
        self.count[rm] -= 1
        if not self.buckets[self.mcnt]:
            self.mcnt -= 1
        return rm


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
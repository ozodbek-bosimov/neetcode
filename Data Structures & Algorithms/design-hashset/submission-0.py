class MyHashSet:

    def __init__(self):
        self.size = 10_007
        self.hashset = [[] for _ in range(self.size)]

    def _getHash(self,num)-> int:
        return num % self.size

    def add(self, key: int) -> None:
        k = self._getHash(key)
        for e in self.hashset[k]:
            if e == key:
                return
        self.hashset[k].append(key)

    def remove(self, key: int) -> None:
        k = self._getHash(key)
        for i, e in enumerate(self.hashset[k]):
            if e == key:
                self.hashset[k].pop(i)
                return
        

    def contains(self, key: int) -> bool:
        k = self._getHash(key)
        for e in self.hashset[k]:
            if e == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
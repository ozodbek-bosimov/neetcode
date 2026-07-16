class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.size = 10_007
        self.hashset = [Node(0) for _ in range(self.size)]


    def _getHash(self,num)-> int:
        return num % self.size

    def add(self, key: int) -> None:
        k = self._getHash(key)
        node = self.hashset[k]
        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = Node(key)

    def remove(self, key: int) -> None:
        k = self._getHash(key)
        node = self.hashset[k]
        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return

    def contains(self, key: int) -> bool:
        k = self._getHash(key)
        node = self.hashset[k]
        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
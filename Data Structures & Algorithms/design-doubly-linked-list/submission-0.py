class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        # T: O(min(index, n-index)) = O(n//2) = O(n)
        if index < 0 or index >= self.size:
            return -1

        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1, index, -1):
                curr = curr.prev
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        # T: O(1)
        new_node = Node(val, self.head)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # T: O(1)
        new_node = Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # T: O(min(index, n-index)) = O(n//2) = O(n)
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        if index < self.size // 2:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
        
        else:
            curr = self.tail

            for _ in range(self.size - 1, index - 1, -1):
                curr = curr.prev

        nxt = curr.next
        new_node = Node(val)

        curr.next = new_node
        new_node.prev = curr

        new_node.next = nxt
        nxt.prev = new_node
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # T: O(min(index, n-index)) = O(n//2) = O(n)
        if index < 0 or index >= self.size:
            return

        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return

        if index == 0:
            self.head = self.head.next
            self.head.prev = None

            self.size -= 1
            return

        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None

            self.size -= 1
            return

        if index < self.size // 2:
            curr = self.head

            for _ in range(index):
                curr = curr.next

        else:
            curr = self.tail

            for _ in range(self.size - 1, index, -1):
                curr = curr.prev

        prev_node = curr.prev
        next_node = curr.next

        prev_node.next = next_node
        next_node.prev = prev_node
        # curr.next = None
        # curr.prev = None

        self.size -= 1



if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.addAtHead(1)
    dll.addAtTail(3)
    dll.addAtIndex(1, 2)
    print(dll.get(1))
    dll.deleteAtIndex(1)
    print(dll.get(1))
    dll.addAtHead(4)
    dll.addAtTail(5)
    print(dll.get(0), dll.get(1), dll.get(2), dll.get(3), dll.get(4), dll.get(5))

"""
  None
  None <-> 1 <-> None
  None <-> 1 <-> 3 <-> None
  None <-> 1 <-> 2 <-> 3 <-> None
  None <-> 1 <-> 3 <-> None
  None <-> 4 <-> 1 <-> 3 <-> None
  None <-> 4 <-> 1 <-> 3 <-> 5 <-> None
"""

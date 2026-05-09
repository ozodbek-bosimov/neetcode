class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        # T: O(n)
        if index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        # T: O(1)
        self.size += 1
        if self.head is None:
            self.head = self.tail = ListNode(val)
            return
        insertNode = ListNode(val, self.head)
        self.head = insertNode


    def insertTail(self, val: int) -> None:
        # T: O(1)
        self.size += 1
        if self.head is None:
            self.head = self.tail = ListNode(val)
            return
        insertNode = ListNode(val)
        self.tail.next = insertNode
        self.tail = insertNode

    def remove(self, index: int) -> bool:
        # T: O(n)
        if index >= self.size:
            return False

        # head
        if index == 0:
            self.head = self.head.next

            if self.size == 1:
                self.tail = None

            self.size -= 1
            return True

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        # tail
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next

        self.size -= 1
        return True
            
    def getValues(self) -> List[int]:
        # T: O(n)
        ans = [0]* self.size

        curr = self.head
        for i in range(self.size):
            ans[i] = curr.val
            curr = curr.next
        
        return ans

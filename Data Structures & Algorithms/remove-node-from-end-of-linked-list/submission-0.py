class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        lr = length - n

        prev = None
        curr = head

        for _ in range(lr):
            prev = curr
            curr = curr.next

        if not prev:
            return head.next

        prev.next = curr.next
        return head
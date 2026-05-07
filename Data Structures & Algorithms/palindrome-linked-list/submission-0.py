# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# T: O(n)
# S: O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        if fast:
            slow = slow.next
        
        while slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        
        return True



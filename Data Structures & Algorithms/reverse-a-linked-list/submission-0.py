# T: O(n)
# S:O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            if curr is None:
                return prev
            next = curr.next
            curr.next = prev
            
            return reverse(curr, next)

        return reverse(None, head)
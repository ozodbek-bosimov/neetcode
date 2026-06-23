# T: O(n) recursion
# S: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        def rec(a, b, steps):
            if steps == 0:
                return b
            return rec(b, a + b, steps - 1)
        
        return rec(2, 3, n - 3)
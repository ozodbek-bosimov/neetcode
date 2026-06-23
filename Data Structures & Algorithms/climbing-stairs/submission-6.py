# T: O(n) iteration
# S: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        a = 2
        b = 3
        for _ in range(n - 3):
            a, b = b, a + b

        return b
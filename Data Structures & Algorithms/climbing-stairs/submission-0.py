# T: O(n) iteration
# S: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        dp = [2,3]
        for _ in range(n-3):
            dp.append(dp[-1] + dp[-2])
        
        return dp[-1]
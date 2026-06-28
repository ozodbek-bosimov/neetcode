class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        
        for r in range(m - 1): #
            row = dp
            for i in range(1,n):
                row[i] += row[i - 1]
            dp = row
        
        return dp[n - 1]
    
    # Time complexity: O(mn)
    # Space complexity: O(n)



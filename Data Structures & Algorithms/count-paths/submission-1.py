class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2)//(math.factorial(m - 1)*math.factorial(n - 1))
    
    # Time complexity: O(m + n)
    # Space complexity: O(1)



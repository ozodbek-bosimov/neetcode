class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        mi = min(m - 1, n - 1)

        for i in range(1, mi + 1):
            ans = ans * (m + n - 2 - mi + i) // i
        return ans
    # Time complexity: O(min(m, n))
    # Space complexity: O(1)



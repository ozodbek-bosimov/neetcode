# Brute-force DFS
# TC: O(3^(mn))
# SC: O(mn)
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        r, c = len(grid), len(grid[0])
        seen = set()
        
        def dfs(i, j, h):
            if i < 0 or r <= i or j < 0 or c <= j:
                return False
            if grid[i][j] == 1:
                h -= 1
            if (i, j) in seen or h == 0:
                return False

            if i == r - 1 and j == c - 1:
                return True
            
            seen.add((i, j))
            up = dfs(i - 1, j, h)
            down = dfs(i + 1, j, h)
            left = dfs(i, j - 1, h)
            right = dfs(i, j + 1, h)
            seen.remove((i, j))

            return up or down or left or right
        
        return dfs(0, 0, health)
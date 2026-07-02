# TC: O((mnh))
# SC: O(mn)
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        r, c = len(grid), len(grid[0])
        best = [[-1] * c for _ in range(r)]
        
        health -= grid[0][0]
        if health <= 0:
            return False
        best[0][0] = health
        queue = deque([(0,0, health)])

        while queue:
            i, j, h = queue.popleft()
            if i == r - 1 and j == c - 1:
                return True

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xi = i + di
                xj = j + dj
                if 0 > xi or xi >= r or 0 > xj or xj >= c:
                    continue
                
                xh = h - grid[xi][xj]
                if xh <= 0 or best[xi][xj] >= xh:
                    continue
                
                best[xi][xj] = xh
                queue.append((xi, xj, xh))

        return False   
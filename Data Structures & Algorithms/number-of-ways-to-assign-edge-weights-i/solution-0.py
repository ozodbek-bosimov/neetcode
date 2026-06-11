# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
from collections import defaultdict, deque

# n = len(edges)
# T: O(n)
# S: O(n)
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 1000000007

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs():
            queue = deque([1])
            seen = {1}
            depth = -1

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for nxt in graph[node]:
                        if nxt not in seen:
                            seen.add(nxt)
                            queue.append(nxt)
                depth += 1

            return depth
        
        d = bfs()

        return pow(2, d - 1, MOD)


if __name__ == "__main__":
    print(Solution().assignEdgeWeights([[1,2]]))
    print(Solution().assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]]))
    print(Solution().assignEdgeWeights([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]]))

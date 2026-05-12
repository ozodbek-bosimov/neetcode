# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

# n = len(tasks)
# T: O(n log n)
# S: O(1)
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: -x[1]+x[0])
        ans = 0
        curr = 0
        for actual, minim in tasks:
            need = minim - curr
            if need > 0:
                ans += need
                curr += need
            curr -= actual
        return ans

if __name__ == "__main__":
    min_energy = Solution().minimumEffort([[1,2],[2,4],[4,8],[6,8]])
    print(min_energy)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, (target - p)/s))
        
        cars.sort(reverse=True)
        
        ans = []
        for pt in cars:
            if not ans or ans[-1] < pt[1]:
                ans.append(pt[1])
        
        return len(ans)

# Time complexity: O(n log n)
# Space complexity: O(n)


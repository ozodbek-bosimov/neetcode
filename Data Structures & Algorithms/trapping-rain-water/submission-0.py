class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        l, r = 0, len(height) - 1

        ans = 0

        while l < r:
            if height[l] < height[r]:
                if left_max < height[l]:
                    left_max = height[l]
                else:
                    ans += left_max - height[l]
                l += 1
            
            else:
                if right_max < height[r]:
                    right_max = height[r]
                else:
                    ans += right_max - height[r]
                r -= 1
        
        return ans
                
            
            

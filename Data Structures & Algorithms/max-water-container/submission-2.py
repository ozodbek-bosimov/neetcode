class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mh = max(heights)
        maxamount = 0
        while l < r:
            maxamount = max(maxamount, (r - l)*min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            if (r - l) * mh < maxamount:
                break
        
        return maxamount
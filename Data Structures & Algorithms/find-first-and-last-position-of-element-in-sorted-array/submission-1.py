class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        start = -1
        while l <= r:
            # O(log n)
            m = (l + r)//2
            if nums[m] == target:
                start = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        if start == -1:
            return [-1,-1]
        

        end = start
        l, r = start, len(nums) - 1
        while l <= r:
            # O(log n)
            m = (l + r)//2
            if nums[m] == target:
                end = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return [start, end]


# TC: O((log n) + (log n)) = O(log n)
# SC: O(1)
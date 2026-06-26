class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        found = -1
        while l <= r:
            # O(log n)
            m = (l + r)//2
            if nums[m] == target:
                found = m
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if found == -1:
            return [-1,-1]
        start = end = found
        while start > 0:
            # O(n)
            if nums[start - 1] == target:
                start -= 1
            else:
                break
        
        while end < len(nums) - 1:
            # O(n)
            if nums[end + 1] == target:
                end += 1
            else:
                break
        
        return [start, end]

# TC: O( log n + n + n) = O(n)
# SC: O(1)

# Example:
nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]
print(Solution().searchRange(nums, target))
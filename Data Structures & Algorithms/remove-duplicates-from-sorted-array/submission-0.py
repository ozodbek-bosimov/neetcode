class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        
        l, r = 1, 1
        while r < n:
            if nums[l - 1] == nums[r]:
                r += 1
            
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        
        return l
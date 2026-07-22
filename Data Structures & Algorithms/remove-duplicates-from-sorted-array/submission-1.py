class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        
        l, r = 0, 1
        while r < n:
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        
        return l + 1
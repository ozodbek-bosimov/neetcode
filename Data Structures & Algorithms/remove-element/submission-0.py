class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = len(nums) - 1
        for i in range(p, -1, -1):
            if nums[i] == val:
                nums[i] = nums[p]
                p -= 1
        
        return p + 1
            
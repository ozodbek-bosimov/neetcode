class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        maxl = 0
        for n in nums:
            if n == 1:
                l += 1
                continue
            elif maxl < l:
                maxl = l
            l = 0
    
        return l if l > maxl else maxl

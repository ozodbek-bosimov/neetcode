class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl = 100_001
        subSum = 0
        l, r = 0, 0

        while r < len(nums):
            subSum += nums[r]
            while target <= subSum:
                minl = min(minl, r - l + 1)
                subSum -= nums[l]
                l += 1

            r += 1
        
        return minl if minl != 100_001 else 0
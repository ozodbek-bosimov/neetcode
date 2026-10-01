class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        target = 1
        for num in nums:
            if num <= 0:
                continue
            
            if num == target:
                target += 1
            elif num > target:
                return target

        return target

# Time: O(N log N)
# Space: O(1) without sorting
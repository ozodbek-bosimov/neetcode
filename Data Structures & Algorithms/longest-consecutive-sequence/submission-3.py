class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        max_l = 1
        l = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                l += 1
            else:
                max_l = max(max_l, l)
                l = 1

        return max(max_l, l)
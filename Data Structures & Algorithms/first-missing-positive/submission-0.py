class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in range(1, 2**31):
            if num not in nums_set:
                return num
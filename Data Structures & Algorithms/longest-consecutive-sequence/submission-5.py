class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numss = set(nums)
        max_l = 0

        for num in numss:
            if num - 1 not in numss:
                l = 1
                curr = num

                while curr + 1 in numss:
                    l += 1
                    curr += 1
                
                max_l = max(max_l, l)

        return max_l
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def numsReverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n

        numsReverse(0, n - 1)
        numsReverse(0, k - 1)
        numsReverse(k, n - 1)

# TC: O(N)
# SC: O(1)
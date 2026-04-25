# Time Complexity : O(n)
# Space Complexity: O(1) extra space 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # sf = [1]
        # for i in range(n - 1):
        #     sf.append(sf[i]*nums[n - 1 - i])
        # sf.reverse()

        # pr = 1
        # for i in range(n):
        #     sf[i] *= pr
        #     pr *= nums[i]

        res = [1] * n
        sf = nums[n - 1]
        for i in range(n - 2, -1, -1):
            res[i] *= sf
            sf *= nums[i]

        pr = nums[0]
        for i in range(1, n):
            res[i] *= pr
            pr *= nums[i]

        return res

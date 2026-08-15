class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pLeftSum = [1]*(n + 1)
        pRightSum = [1]*(n + 1)

        for i in range(n):
            pLeftSum[i + 1] = pLeftSum[i] * nums[i]
            pRightSum[i + 1] = pRightSum[i] * nums[n - i - 1]
        pRightSum.reverse()
        
        for i in range(n):
            pLeftSum[i] *= pRightSum[i + 1]
        pLeftSum.pop()
        return pLeftSum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}

        s = 0
        ans = 0
        for num in nums:
            s += num
            ans += prefix.get(s - k, 0)
            prefix[s] = prefix.get(s, 0) + 1
        
        return ans


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)//2
        count = Counter()
        for n in nums:
            count[n] += 1
            if count[n] > limit:
                return n
        
        
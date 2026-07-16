class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = collections.Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for num, count in nums_count.items():
            bucket[count].append(num)
        
        ans = []
        for i in range(n, -1, -1):
            while bucket[i]:
                ans.append(bucket[i].pop())

                if len(ans) == k:
                    return ans
            
        
        return ans
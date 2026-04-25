# n - nums.length
# Time Complexity : O(n)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for num, freq in nums_count.items():
            bucket[freq].append(num)
        ans = []
        # for i in range(n, -1, -1):
        #     if len(ans) >= k:
        #         break
        #     while bucket[i] and len(ans) < k:
        #         ans.append(bucket[i].pop())
        for i in range(n, -1, -1):
            while bucket[i]:
                ans.append(bucket[i].pop())
                if len(ans) == k:
                    return ans
        
        return ans



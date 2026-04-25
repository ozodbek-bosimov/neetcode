# n - nums.length
# Time Complexity: O(n + n*log k + k) = O(n*log k)
# Space Complexity: O(2*n + 2*k + k) = O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        heap = []
        for num, freq in nums_count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
                continue
            heapq.heappushpop(heap, (freq, num))

        return [num for freq, num in heap]

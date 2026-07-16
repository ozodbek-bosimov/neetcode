class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = collections.Counter(nums)
        heap = []
        for num, count in nums_count.items():
            
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
                continue
            
            heapq.heappushpop(heap, (count, num))

        return [num for c, num in heap]
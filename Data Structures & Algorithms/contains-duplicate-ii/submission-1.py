# T: O(n) 11 ms
# S: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        if len(nums) <= k + 1:
            return True
        
        last_seen_index = {}
        for i, num in enumerate(nums):
            if num in last_seen_index and i  <= k + last_seen_index[num]:
                return True
            
            last_seen_index[num] = i
        
        return False
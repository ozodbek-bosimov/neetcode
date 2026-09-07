class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window  = Counter(nums[:k+1])
        for v in window.values():
            if v >= 2:
                return True
        
        for i in range(k+1, len(nums)):
            window[nums[i]] += 1
            window[nums[i - k - 1]] -= 1

            if window[nums[i - k - 1]]  == 0:
                del window[nums[i - k - 1]]
            
            if window[nums[i]] >= 2:
                return True
        
        return False
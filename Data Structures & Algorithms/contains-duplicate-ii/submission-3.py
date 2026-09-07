class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = Counter(nums[: k+1])
        for v in window.values():
            if v >= 2:
                return True
            
        for i in range(k + 1, len(nums)):
            add = nums[i]
            rm = nums[i - k - 1]
            window[add] += 1
            window[rm] -= 1

            if window[rm] == 0:
                del window[rm]
            if window[add] == 2 :
                return True
        
        return False
            
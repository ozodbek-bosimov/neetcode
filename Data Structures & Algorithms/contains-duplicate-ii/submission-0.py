# T: O(n) 131 ms
# S: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = Counter(nums[:k+1])
        for val in window.values():
            if val >= 2:
                return True
        
        for i in range(k+1, len(nums)):
            add = nums[i]
            rem = nums[i - k - 1]
            window[add] += 1
            window[rem] -= 1
            
            if window[rem] <= 0:
                del window[rem]
            
            if window[add] == 2:
                return True
            
        return False


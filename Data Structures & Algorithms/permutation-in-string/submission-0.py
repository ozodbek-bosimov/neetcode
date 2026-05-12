# https://leetcode.com/problems/permutation-in-string/
from collections import Counter


# T: O(l_s2)
# S: O(1) extra space
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1, l_s2 = len(s1), len(s2)
        if l_s1 > l_s2:
            return False
        
        letter_count_s1 = Counter(s1)
        window = Counter(s2[:l_s1])
        if letter_count_s1 == window: return True
        
        for i in range(l_s1, l_s2):
            add = s2[i]
            remove = s2[i - l_s1]
            window[add] += 1
            window[remove] -= 1
            if window[remove] == 0: 
                del window[remove]
            if window == letter_count_s1: 
                return True
        
        return False

# example:
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo")) # True 
print(sol.checkInclusion("ab", "eidboaoo")) # False

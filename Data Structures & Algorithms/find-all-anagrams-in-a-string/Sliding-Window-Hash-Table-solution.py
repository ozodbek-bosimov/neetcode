# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter

# T: O(ls + lp)
# S: O(1) extra space
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls,lp = len(s), len(p)
        window, need = Counter(s[:lp]), Counter(p)
        
        ans = []
        if need == window:
            ans.append(0)
    
        for i in range(lp, ls):
            pop = s[i - lp]
            add = s[i]
            window[pop] -= 1
            window[add] += 1

            if window[pop] == 0:
                del window[pop]
            
            if need == window:
                ans.append(i - lp + 1)
        
        return ans

# example:
sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc")) # [0, 6]
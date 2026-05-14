# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# T: O(ls + lp)
# S: O(1) extra space
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls,lp = len(s), len(p)
        if lp > ls: return []
        window, need = [0] * 26, [0] * 26
        for i in range(lp):
            window[ord(s[i]) - 97] += 1
            need[ord(p[i]) - 97] += 1
        
        ans = []
        if need == window:
            ans.append(0)
        for i in range(lp, ls):
            pop = s[i - lp]
            add = s[i]
            window[ord(pop) - 97] -= 1
            window[ord(add) - 97] += 1
            
            if need == window:
                ans.append(i - lp + 1)
        
        return ans
# example:
sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc")) # [0, 6]
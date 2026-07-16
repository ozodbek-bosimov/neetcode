class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr = min(strs, key = lambda x: len(x))
        
        for i, ch in enumerate(minstr):

            for s in strs:
                if s[i] != ch:
                    return minstr[:i]
        
        return minstr

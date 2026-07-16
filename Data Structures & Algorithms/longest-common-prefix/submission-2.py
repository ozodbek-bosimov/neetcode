class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = min(strs)
        last  = max(strs)

        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
        return first[:i]

        

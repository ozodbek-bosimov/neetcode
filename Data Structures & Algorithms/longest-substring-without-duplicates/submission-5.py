class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        longest_length = 0
        for r, v in enumerate(s):
            if v in seen and l <=  seen[v]:
                l = seen[v] + 1
            longest_length = max(longest_length, r - l + 1)
            seen[v] = r

        return longest_length

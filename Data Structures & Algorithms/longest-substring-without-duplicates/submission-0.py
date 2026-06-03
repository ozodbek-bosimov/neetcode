# N = s.length
# T: O(N)
# S: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        left = 0
        table = {}
        for i, ch in enumerate(s):
            if ch in table and table[ch] >= left:
                longest_length = max(longest_length, i - left)
                left = table[ch] + 1
            table[ch] = i
        longest_length = max(longest_length, len(s) - left)
        return longest_length
# https://leetcode.com/problems/score-of-a-string/

# n -> number of characters in the string
# Time: O(n)  — iterate through string once
# Space: O(1) — constant extra space
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev_val = ord(s[0])

        for ch in s[1:]:
            curr_val = ord(ch)
            res += abs(curr_val - prev_val)
            prev_val = curr_val

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfString("zaz")) # 50

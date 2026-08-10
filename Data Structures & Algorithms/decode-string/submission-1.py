# n = s.length
# T: O(n)
# S: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                stack.append((res, num))
                res = ""
                num = 0
            elif ch == "]":
                prev, count = stack.pop()
                res = prev + count * res

            else:
                res += ch

        return res

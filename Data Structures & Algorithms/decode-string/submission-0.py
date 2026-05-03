# n = s.length
# T: O(n)
# S: O(n)
class Solution:
    def decodeString(self, s: str) -> str:  # "3[a]2[bc]"
        stack = []  # (aaa, 2)
        num = 0  # 0
        res = ""  # bc

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)  # 2

            elif ch == "[":
                stack.append((res, num))
                res = ""
                num = 0
            elif ch == "]":
                prev, count = stack.pop()
                res = prev + count * res  # aaa + 2*bc

            else:
                res += ch  # c

        return res  # aaabcbc

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closes = {')': '(', '}': '{',  ']': '['}

        for ch in s:
            if ch in closes:
                if stack and stack[-1] == closes[ch]:
                    stack.pop()
                    continue
                return False
            
            stack.append(ch)
        
        return len(stack) == 0
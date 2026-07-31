class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        res = 0
        for op in ops:
            if op == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                res += stack[-1]*2
                stack.append(stack[-1]*2)
            elif op == 'C':
                rm = stack.pop()
                res -= rm
            else:
                stack.append(int(op))
                res += int(op)
        
        return res

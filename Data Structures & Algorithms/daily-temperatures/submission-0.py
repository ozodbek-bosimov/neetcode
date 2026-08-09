class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        n = len(temperatures)
        ans = [0]* n

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                previ = stack.pop()
                ans[previ] = i - previ
            stack.append(i)
        return ans
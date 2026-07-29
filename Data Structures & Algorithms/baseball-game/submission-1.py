class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        res = 0
        for op in operations:
            if op == "+":
                res += points[-1]+ points[-2]
                points.append(points[-1]+ points[-2])

            elif op == "D":
                res += points[-1]*2
                points.append(points[-1]*2)

            elif op == "C":
                pn = points.pop()
                res -= pn

            else:
                points.append(int(op))
                res += int(op)
        
        return sum(points)
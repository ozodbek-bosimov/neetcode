class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in boxes[r//3*3 + c//3] or num in rows[r] or num in cols[c]:
                    return False
                
                boxes[r//3*3 + c//3].add(num)
                rows[r].add(num)
                cols[c].add(num)

        return True
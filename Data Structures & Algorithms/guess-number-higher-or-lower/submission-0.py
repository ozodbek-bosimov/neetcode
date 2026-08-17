class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            num = (low + high) // 2 
            res = guess(num)
            if res == 0:
                return num 
            elif res == -1:
                high = num-1 
            else:
                low = num + 1
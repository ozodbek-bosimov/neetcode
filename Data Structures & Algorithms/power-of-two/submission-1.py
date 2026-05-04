# T: O(log n)
# S: O(1)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
        
#         while n & 1 == 0:
#             n = n >> 1
#         return n == 1


# –––––––––––––––––––––––––––––––––––
#  n = 16 = 2^4 -> 10000 &
#  n - 1 = 15   -> 01111
                #  –––––
                #  00000
#  n > 0
#  n & (n - 1) == 0  √√

# T: O(1)
# S: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

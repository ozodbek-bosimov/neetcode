#  https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        max_right = -1
        for i in range(n-1, -1, -1):
            this_val = arr[i]
            arr[i] = max_right
            if this_val > max_right:
                max_right = this_val
        
        return arr
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.replaceElements([17,18,5,4,6,1]))


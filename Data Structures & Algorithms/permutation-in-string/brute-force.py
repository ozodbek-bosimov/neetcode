# T: O(l_s1*log l_s1  + (l_s2 - l_s1 + 1)*(l_s1*log l_s1 + l_s1)) = O(l_s1*log l_s1 + l_s2*l_s1*log l_s1 - l_s2*l_s1 - l_s1^2*log l_s1 - l_s1^2 + l_s1*log l_s1 + l_s1) =
# = O(l_s2*l_s1*log l_s1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1 = len(s1)
        l_s2 = len(s2)
        if l_s1 > l_s2:
            return False
        
        sorted_s1 = sorted(s1)
        for i in range(l_s1, l_s2 + 1):
            if sorted(s2[i - l_s1 : i]) == sorted_s1:
                return True
        
        return False


# example:
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo")) # True 
print(sol.checkInclusion("ab", "eidboaoo")) # False
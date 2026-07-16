class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        count = [0]*26
        for i in range(n):
            count[ord(s[i]) - 97] += 1
            count[ord(t[i]) - 97] -= 1
        
        for c in count:
            if c != 0:
                return False
        
        return True
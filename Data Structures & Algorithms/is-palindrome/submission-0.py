class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isInsensitive(ch: str) -> bool:
            n = ord(ch)
            if 65 <= n <= 90 or 97<= n <= 122 or 48 <= n <= 57:
                return True
        
            return False
        
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isInsensitive(s[l]):
                l += 1
            
            while l < r and not isInsensitive(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True

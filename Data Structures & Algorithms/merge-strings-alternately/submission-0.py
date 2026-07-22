class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = 0
        n1 = len(word1)
        l2 = 0
        n2 = len(word2)

        ans = []
        while l1 < n1 and l2 < n2:
            ans.append(word1[l1])
            ans.append(word2[l2])
            l1 += 1
            l2 += 1
        
        return "".join(ans) + word1[l1:] + word2[l2:]
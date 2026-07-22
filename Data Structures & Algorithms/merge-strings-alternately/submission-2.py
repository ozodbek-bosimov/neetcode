class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        s = ""

        if l1 > l2:
            n = l2
            m = l1
            w = word1
        else:
            n = l1
            m = l2
            w = word2

        for i in range(n):
            s = s + word1[i] + word2[i]

        s = s + w[n:m]
        return s
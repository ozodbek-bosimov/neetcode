class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for w in strs:
            ans.append(f'{len(w)}*{w}')
        print(ans)
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        ans = []
        i, n = 0, len(s)
        while i < n:
            num = 0
            while s[i] != '*':
                num = 10*num + int(s[i])
                i += 1
            i += 1
            w = s[i: i + num]
            ans.append(w)
            i += num

        return ans     

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(arr)- 1, -1, -1):
            mp[abs(x - arr[i])].append(arr[i])
        r = sorted(mp.keys())
        
        ans = []
        for key in r:
            while mp[key] and k > 0:
                ans.append(mp[key].pop())
                k -= 1
            if k == 0:
                break
        ans.sort()
        return ans






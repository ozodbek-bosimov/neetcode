class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        usrs_wbs = list(zip(timestamp, username, website))
        usrs_wbs.sort()
        
        usrs = {}
        for t, usr, wb in usrs_wbs:
            usrs[usr] = usrs.get(usr, [])
            usrs[usr].append(wb)
        
        count = {}
        for usr, wbs in usrs.items():
            patterns = set()
            
            n = len(wbs)
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        patterns.add((wbs[i], wbs[j], wbs[k]))
            
            for pattern in patterns:
                count[pattern] = count.get(pattern, 0) + 1
            
        max_pattern = ()
        max_score = 0
        for p, s in count.items():
            if s > max_score or (s == max_score and p < max_pattern):
                max_pattern = p
                max_score = s

        return list(max_pattern)
        
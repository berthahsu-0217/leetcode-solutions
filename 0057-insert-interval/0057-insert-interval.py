class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        s0, e0 = newInterval
        inserted = False
        ans = []
        
        for s, e in intervals:
            if inserted or e < s0:
                ans.append([s,e])
            elif e0 < s:
                ans.append([s0,e0])
                ans.append([s,e])
                inserted = True
            else:
                s0 = min(s, s0)
                e0 = max(e, e0)
        
        if not inserted:
            ans.append([s0, e0])
        
        return ans
        
            
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        """
        [[0,2],[2,4],[3,5],[4,6]]
        
        ans 1
         2    4
        s0   e0
           s     e
              s     e   
        """
        ans = 0
        intervals.sort()
        s0, e0 = intervals[0]
        
        n = len(intervals)
        for i in range(1, n):
            s, e = intervals[i]
            if s < e0: #overlapping intervals
                e0 = min(e, e0)
                ans += 1
            else:
                s0, e0 = s, e
                
        return ans
            
        
        
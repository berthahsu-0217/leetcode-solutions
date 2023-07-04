class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        
        T = [False]*2001
        
        tasks.sort(key = lambda x: (x[1], x[0]))
        
        ans = 0
        for s, e, d in tasks:
            for i in range(s, e+1):
                if T[i]:
                    d -= 1
            while d > 0:
                if not T[i]:
                    T[i] = True
                    d -= 1
                    ans += 1
                i -= 1
        
        return ans
        
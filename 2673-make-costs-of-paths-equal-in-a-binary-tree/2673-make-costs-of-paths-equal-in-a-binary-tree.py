class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        self.ans = 0
        
        def dfs(i):
            #none
            if i >= n:
                return 0
            
            lc = dfs(i*2+1)
            rc = dfs(i*2+2)
            self.ans += abs(lc-rc)
            
            return max(lc,rc)+cost[i]
            
        dfs(0)
        return self.ans
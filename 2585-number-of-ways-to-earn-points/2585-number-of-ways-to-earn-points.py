class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        
        MOD = 10**9+7
        
        """
        i: index in types
        k: possible score choosing before (including) i
        """
        n = len(types)
        dp = [[0 for k in range(target+1)] for i in range(n)]
        
        sc = 0
        for j in range(types[0][0]+1):
            if sc <= target:
                dp[0][sc] = 1
                sc += types[0][1]
        
        for i in range(1, n):
            add = 0
            for j in range(types[i][0]+1):
                for k in range(target+1):
                    if dp[i-1][k] > 0 and (k+add) <= target:
                        dp[i][k+add] += dp[i-1][k]
                        dp[i][k+add] %= MOD
                add += types[i][1]
        
        return dp[n-1][target]
            
        
            
        
        
        
                
        
        
                
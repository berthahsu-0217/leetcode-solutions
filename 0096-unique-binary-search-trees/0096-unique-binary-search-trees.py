class Solution:
    def numTrees(self, n: int) -> int:

        dp = [None for i in range(n+1)]
        
        return self.construct(n, dp)
        
    
    def construct(self, n, dp):
        
        if dp[n] is not None:
            return dp[n]
        
        if n <= 1:
            return 1
        
        cnt = 0
        for i in range(1, n+1):
            cnt += self.construct(i-1, dp)*self.construct(n-i, dp)
            
        dp[n] = cnt
            
        return cnt
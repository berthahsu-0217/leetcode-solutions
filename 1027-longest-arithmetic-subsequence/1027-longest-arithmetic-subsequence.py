class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        n = len(A)
        
        dp = [dict() for i in range(n)]
        
        maxLens = 0
        
        for i in range(n-1):
            for j in range(i+1, n):
                diff = A[j]-A[i]
                if diff in dp[i]:
                    dp[j][diff] = max(dp[j].get(diff, 0), dp[i][diff]+1)
                else:
                    dp[j][diff] = 2
                maxLens = max(maxLens, dp[j][diff])
                
        return maxLens
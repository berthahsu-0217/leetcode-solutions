class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        """
        deletion   replacement
          |       /
        e 5
        s 4
        r 3
        o 2
        h 1 1 2 
        " 0 1 2 3 -- insertion
          " r o s 
        """
        m, n = len(word1), len(word2)
        dp = [[None for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = 0
        
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0]+1
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1]+1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                d1 = dp[i-1][j-1] + (word1[i-1] != word2[j-1])
                d2 = dp[i-1][j]+1
                d3 = dp[i][j-1]+1
                dp[i][j] = min(d1, d2, d3)
        
        return dp[m][n]
        

        
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):

                if obstacleGrid[i][j] == 1:
                    continue  
    
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    
                #print(dp)
                
        return dp[m-1][n-1]
        
        
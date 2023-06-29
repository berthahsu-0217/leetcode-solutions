import heapq as hq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[float("inf") for j in range(n)] for i in range(m)]
        dp[0][0] = 0
        
        heap = [(0,0,0)]
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        while heap:
            d, x, y = hq.heappop(heap)
            if x == m-1 and y == n-1:
                return d
            if dp[x][y] != d:
                continue
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and d+int(grid[nx][ny] == 1) < dp[nx][ny]:
                    dp[nx][ny] = d+int(grid[nx][ny] == 1)
                    hq.heappush(heap, (dp[nx][ny], nx, ny))
        
        return -1
                    
            
        

        
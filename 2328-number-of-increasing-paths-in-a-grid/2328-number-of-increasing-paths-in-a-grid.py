class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        @cache
        def dfs(x, y):
            paths = 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                    paths += dfs(nx, ny)
                    paths %= MOD
            return paths
        
        MOD = 1000000007
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
                ans %= MOD
        
        return ans % MOD
        
        
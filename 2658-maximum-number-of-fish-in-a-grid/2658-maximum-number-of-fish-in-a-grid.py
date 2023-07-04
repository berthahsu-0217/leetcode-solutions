class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            cnt = 0
            visited.add((x, y))
            cnt += grid[x][y]
            
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0 and (nx, ny) not in visited:
                    cnt += dfs(nx, ny)
            
            return cnt
                    
        visited = set()
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        max_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in visited:
                    max_cnt = max(max_cnt, dfs(i, j))
        
        return max_cnt
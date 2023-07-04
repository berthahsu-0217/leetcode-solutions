class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        @cache
        def dfs(x, y):
            
            max_l = 0
            #(row - 1, col + 1), (row, col + 1) and (row + 1, col + 1)
            if 0 <= x-1 < m and 0 <= y+1 < n and grid[x-1][y+1] > grid[x][y]:
                max_l = max(max_l, dfs(x-1, y+1))
            if 0 <= x < m and 0 <= y+1 < n and grid[x][y+1] > grid[x][y]:
                max_l = max(max_l, dfs(x, y+1))
            if 0 <= x+1 < m and 0 <= y+1 < n and grid[x+1][y+1] > grid[x][y]:
                max_l = max(max_l, dfs(x+1, y+1))
            
            return max_l+1
        
        ans = 0
        for i in range(m):
            ans = max(ans, dfs(i, 0))
        
        return ans-1
                
                
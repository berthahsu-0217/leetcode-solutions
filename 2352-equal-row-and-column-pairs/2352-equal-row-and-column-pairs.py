class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        ans = 0
        n = len(grid)
        key_to_rows = dict()
        
        for i in range(n):
            key = tuple(grid[i])
            key_to_rows[key] = key_to_rows.get(key, 0)+1
        
        for j in range(n):
            key = tuple([grid[i][j] for i in range(n)])
            ans += key_to_rows.get(key, 0)
        
        return ans
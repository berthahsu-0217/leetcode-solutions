class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        
        prefix = [[set() for j in range(n)] for i in range(m)]
        suffix = [[set() for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    prefix[i][j] = set([x for x in prefix[i-1][j-1]])
                prefix[i][j].add(grid[i][j])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1 and j < n-1:
                    suffix[i][j] = set([x for x in suffix[i+1][j+1]])
                suffix[i][j].add(grid[i][j])
                    
        #print(prefix)
        #print(suffix)
        
        ans = [[0 for j in range(n)] for i in range(m)]
                  
        for i in range(m):
            for j in range(n):
                  x = len(prefix[i-1][j-1]) if i > 0 and j > 0 else 0
                  y = len(suffix[i+1][j+1]) if i < m-1 and j < n-1 else 0
                  ans[i][j] = abs(x-y)
        
        return ans
                
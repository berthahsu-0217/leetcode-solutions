class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        memo = dict()
        
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                memo[mat[i][j]] = [i, j]
                
        rows = [0]*m
        cols = [0]*n
        
        for i in range(len(arr)):
            x, y = memo[arr[i]]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m:
                return i
        
        return n-1
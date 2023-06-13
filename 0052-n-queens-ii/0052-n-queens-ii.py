class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def dfs(i, n, row, col, diag1, diag2):
            if i >= n:
                return 1
            nways = 0
            for j in range(n):
                if row[i] or col[j] or diag1[i+j] or diag2[i-j+n-1]:
                    continue
                row[i] = col[j] = diag1[i+j] = diag2[i-j+n-1] = True
                nways += dfs(i+1, n, row, col, diag1, diag2)
                row[i] = col[j] = diag1[i+j] = diag2[i-j+n-1] = False
            return nways
        
        row = [False]*n
        col = [False]*n
        diag1 = [False]*(2*n-1)
        diag2 = [False]*(2*n-1)
        return dfs(0, n, row, col, diag1, diag2)
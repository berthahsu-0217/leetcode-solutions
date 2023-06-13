class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        #time complexity: O(n! + R * n^2), R: # of solutions
        #space complexity: O(n + R * n^2)
        
        def dfs(x, n, board, row, col, diag1, diag2, ans):
            
            if x >= n:
                ans.append(["".join(board[i]) for i in range(n)])
                return
            
            for y in range(n):
                if not (row[x] or col[y] or diag1[x+y] or diag2[y-x+n-1]):
                    row[x] = col[y] = diag1[x+y] = diag2[y-x+n-1] = True
                    board[x][y] = 'Q'
                    dfs(x+1, n, board, row, col, diag1, diag2, ans)
                    row[x] = col[y] = diag1[x+y] = diag2[y-x+n-1] = False
                    board[x][y] = '.'
                
            return
        
        board = [['.' for i in range(n)] for i in range(n)]
        row = [False]*n
        col = [False]*n
        #i:x+y
        diag1 = [False]*(2*n-1)
        #i:y-x+n-1
        diag2 = [False]*(2*n-1)
        
        ans = []
        dfs(0, n, board, row, col, diag1, diag2, ans)
        
        return ans
        
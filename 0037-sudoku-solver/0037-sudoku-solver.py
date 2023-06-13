class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        time complexity: O(9! ^ 9)
        """
        def dfs(i, n, empty, row, col, box, board):
            
            #all empty are filled
            if i >= n:
                return True
            
            x, y = empty[i]
            for d in range(1,10):
                if not (row[x][d] or col[y][d] or box[x//3][y//3][d]):
                    row[x][d] = col[y][d] = box[x//3][y//3][d] = True
                    board[x][y] = str(d)
                    if dfs(i+1, n, empty, row, col, box, board):
                        return True
                    row[x][d] = col[y][d] = box[x//3][y//3][d] = False
                    board[x][y] = "."
            
            return False
        
        row = [[False]*10 for i in range(9)]
        col = [[False]*10 for i in range(9)]
        #i,j:x//3,y//3
        box = [[[False]*10 for j in range(3)] for i in range(3)]
        
        empty = []
        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d != ".":
                    d = int(d)
                    row[i][d] = col[j][d] = box[i//3][j//3][d] = True
                else:
                    empty.append([i,j])
        
        dfs(0, len(empty), empty, row, col, box, board)
        
        
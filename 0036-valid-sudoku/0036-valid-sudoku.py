class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col = [[False for i in range(10)] for j in range(9)]
        row = [[False for i in range(10)] for j in range(9)]
        box = [[[False for i in range(10)] for j in range(3)] for k in range(3)]
        
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    x = int(x)
                    if col[j][x] or row[i][x] or box[i//3][j//3][x]:
                        return False
                    col[j][x] = row[i][x] = box[i//3][j//3][x] = True
        
        return True
                
                    
                    
        
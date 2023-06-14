class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        
        first_row = False
        first_col = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    else:
                        matrix[i][0] = 0
                    if j == 0:
                        first_col = True
                    else:
                        matrix[0][j] = 0
                        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
       
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
                
        return
                        
                    
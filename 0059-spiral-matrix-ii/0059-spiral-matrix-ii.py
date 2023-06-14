class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[None for j in range(n)] for i in range(n)]
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        i = 0
        x, y = 0, 0
        limit = n*n
        
        val = 1
        while val < limit:
            mat[x][y] = val
            val += 1
            while not (0 <= x+dx[i] < n and 0 <= y+dy[i] < n and mat[x+dx[i]][y+dy[i]] is None):
                i = (i+1) % 4
            x, y = x+dx[i], y+dy[i]
        mat[x][y] = limit
        
        return mat
                
            
        
        
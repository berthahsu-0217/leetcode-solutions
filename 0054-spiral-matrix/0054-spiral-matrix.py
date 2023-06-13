class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []
        m, n = len(matrix), len(matrix[0])
        minX, maxX, minY, maxY = 0, m-1, 0, n-1
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        i = 0
        
        x0 = y0 = None
        x = y = 0
        
        for t in range(0, m*n):
            if x0 is None: 
                x0, y0 = x, y
            ans.append(matrix[x][y])
            if t == m*n-1: return ans
            while not (minX <= x+dx[i] <= maxX and minY <= y+dy[i] <= maxY) or (x+dx[i]==x0 and y+dy[i] == y0): 
                if x+dx[i] == x0 and y+dy[i] == y0:
                    minX, maxX, minY, maxY = minX+1, maxX-1, minY+1, maxY-1
                    x0 = y0 = None
                i = (i+1) % 4
                #print(x+dx[i], y+dy[i], x0, y0)
            x, y = x+dx[i], y+dy[i]
            
        return ans
            
        
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if self.dfs(i,j,m,n,board,set(),0,len(word),word):
                    return True
                
        return False
    
    def dfs(self, x, y, m, n, board, explored, idx, lens, word):
        
        if board[x][y] != word[idx]:
            return False
        
        if idx == lens-1:
            return True
        
        explored.add((x,y))
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and (nx,ny) not in explored:
                if self.dfs(nx,ny,m,n,board,explored,idx+1,lens,word):
                    return True
                
        explored.remove((x,y))
        
        return False
                
                    
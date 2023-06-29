import queue

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        x0 = y0 = None
        keys = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '@':
                    x0, y0 = x, y
                elif grid[x][y].isalpha() and grid[x][y].islower():
                    keys += 1
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        q = queue.Queue()
        q.put((x0, y0, 0, 0))
        visited = set()
        visited.add((x0, y0, 0))
        final = 2**keys-1
        
        while not q.empty():
            x, y, moves, bitmask = q.get()
            if bitmask == final:
                return moves
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                    if grid[nx][ny].isalpha() and grid[nx][ny].islower():
                        k = ord(grid[nx][ny])-ord('a')
                        if (nx, ny, bitmask|(1<<k)) not in visited:
                            q.put((nx, ny, moves+1, bitmask|(1<<k)))
                            visited.add((nx, ny, bitmask|(1<<k)))
                    elif grid[nx][ny].isalpha() and grid[nx][ny].isupper():
                        k = ord(grid[nx][ny])-ord('A')
                        if (nx, ny, bitmask) not in visited and bitmask & (1 << k) != 0: #key found already
                            q.put((nx, ny, moves+1, bitmask))
                            visited.add((nx, ny, bitmask))
                    elif (nx, ny, bitmask) not in visited:
                        q.put((nx, ny, moves+1, bitmask))
                        visited.add((nx, ny, bitmask))
                        
        return -1
                            
                            
                    
        
                    
        
        
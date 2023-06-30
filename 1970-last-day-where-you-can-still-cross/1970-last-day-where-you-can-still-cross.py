class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def find_root(disjoint_set, v):
            if disjoint_set[v] != v:
                disjoint_set[v] = find_root(disjoint_set, disjoint_set[v])
            return disjoint_set[v]
        
        def union_by_rank(disjoint_set, rank, u, v):
            r1 = find_root(disjoint_set, u)
            r2 = find_root(disjoint_set, v)
            if rank[r1] > rank[r2]:
                disjoint_set[r2] = r1
            elif rank[r1] < rank[r2]:
                disjoint_set[r1] = r2
            else:
                disjoint_set[r2] = r1
                rank[r1] += 1
        
        #extra node for start(x == 0) and final(x == n-1)
        V = row*col+2
        disjoint_set = [i for i in range(V)]
        rank = [1 for i in range(V)]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        lands = set()
        n = len(cells)
        for i in range(n-1,-1,-1):
            if find_root(disjoint_set, 0) == find_root(disjoint_set, 1):
                return i+1 #return last day
            x, y = cells[i][0]-1, cells[i][1]-1
            if x == 0:
                union_by_rank(disjoint_set, rank, x*col+y+2, 0)
            elif x == row-1:
                union_by_rank(disjoint_set, rank, x*col+y+2, 1)
            lands.add((x,y))
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < row and 0 <= ny < col and (nx, ny) in lands:
                    union_by_rank(disjoint_set, rank, x*col+y+2, nx*col+ny+2)
        return 0
                
        
                            
                    
        
        
        
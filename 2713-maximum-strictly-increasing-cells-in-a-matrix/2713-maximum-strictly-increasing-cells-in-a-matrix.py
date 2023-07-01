import heapq as hq
from collections import deque

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        
        m, n = len(mat), len(mat[0])
        indegrees = [[set() for y in range(n)] for x in range(m)]
        outdegrees = [[set() for y in range(n)] for x in range(m)]
        
        for x in range(m):
            memo = dict()
            for y in range(n):
                if mat[x][y] not in memo:
                    memo[mat[x][y]] = set()
                memo[mat[x][y]].add(y)
            arr = [[k,v] for k, v in memo.items()]
            arr.sort()
            for i in range(1, len(arr)):
                for yy in arr[i-1][1]:
                    for y in arr[i][1]:
                        indegrees[x][y].add((x,yy))
                        outdegrees[x][yy].add((x,y))
            

        for y in range(n):
            memo = dict()
            for x in range(m):
                if mat[x][y] not in memo:
                    memo[mat[x][y]] = set()
                memo[mat[x][y]].add(x)
            arr = [[k,v] for k, v in memo.items()]
            arr.sort()
            for i in range(1, len(arr)):
                for xx in arr[i-1][1]:
                    for x in arr[i][1]:
                        indegrees[x][y].add((xx,y))
                        outdegrees[xx][y].add((x,y))
        
        max_len = [[0 for y in range(n)] for x in range(m)]
        
        q = deque([])
        for x in range(m):
            for y in range(n):
                if len(indegrees[x][y]) == 0:
                    q.append([x,y])
                    max_len[x][y] = 1
        
        #print(q)
        max_path = 1
        while q:
            x, y = q.popleft()
            max_path = max(max_path, max_len[x][y])
            for nx, ny in outdegrees[x][y]:
                indegrees[nx][ny].remove((x, y))
                if len(indegrees[nx][ny]) == 0:
                    q.append([nx,ny])
                max_len[nx][ny] = max(max_len[nx][ny], max_len[x][y]+1)
        
        
        return max_path
            
        
        
        
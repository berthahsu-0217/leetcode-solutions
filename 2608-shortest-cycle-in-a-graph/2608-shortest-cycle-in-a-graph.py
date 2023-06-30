from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        #A cycle can be seen as two shortest paths (with different parents) meet at a point

        def bfs(start):
            
            min_cycle = 1001
            dist = {start:0}
            parent = {start:-1}
            q = deque([start])
            
            while q:
                node = q.popleft()
                #visited.add(node)
                for child in graph[node]:
                    #unvisited
                    if child not in dist:
                        dist[child] = dist[node]+1
                        parent[child] = node
                        q.append(child)
                    #visited before by other paths rather than the current parent
                    elif parent[node] != child and parent[child] != node:
                        #print(V, E)
                        min_cycle = min(min_cycle, dist[node]+dist[child]+1)
            
            return min_cycle
        
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        #visited = set()
        min_cycle = 1001
        for i in range(n):
            #if i not in visited:
            min_cycle = min(min_cycle, bfs(i))
        
        if min_cycle == 1001:
            return -1
        
        return min_cycle
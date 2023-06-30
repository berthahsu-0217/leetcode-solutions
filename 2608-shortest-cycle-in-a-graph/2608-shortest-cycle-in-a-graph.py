class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        def dfs(src, tgt):
            """Checks for path from src to tgt."""
            if src in visited:
                return
            visited.add(src)
            if src == tgt:
                return True
            return any(dfs(nei, tgt) for nei in graph[src])
        
        def bfs(src, tgt):
            """Shortest path from src to tgt."""
            seen = {src}
            q = collections.deque([(src, 0)])
            while q:
                curr, dist = q.popleft()
                if curr == tgt:
                    return dist
                for nei in graph[curr]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, dist + 1))
        
        graph = collections.defaultdict(list)
        res = math.inf
        for u, v in edges:
            visited = set()
            if u in graph and v in graph:
                if dfs(u, v):
                    res = min(res, bfs(u, v))
            graph[u].append(v)
            graph[v].append(u)
        
        # Add 1 for the edge that caused the cycle
        return res + 1 if res < math.inf else -1
"""
import queue

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        #A cycle can be seen as two shortest paths (with different parents) meet at a point

        def bfs(start):
            
            min_cycle = float("inf")
            dist = [float("inf")]*n
            dist[start] = 0
            parent = [-1]*n
            q = queue.Queue()
            q.put(start)
            
            V = 0
            E = 0
            while not q.empty():
                node = q.get()
                #visited.add(node)
                V += 1
                E += len(graph[node])
                for child in graph[node]:
                    #unvisited
                    if dist[child] == float("inf"):
                        dist[child] = dist[node]+1
                        parent[child] = node
                        q.put(child)
                    #visited before by other paths rather than the current parent
                    elif parent[node] != child and parent[child] != node:
                        #print(V, E)
                        return dist[node]+dist[child]+1
            
            return min_cycle
        
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        #visited = set()
        min_cycle = float("inf")
        for i in range(n):
            #if i not in visited:
            min_cycle = min(min_cycle, bfs(i))
            if min_cycle == 3:
                return 3
        
        if min_cycle == float("inf"):
            return -1
        
        return min_cycle
"""
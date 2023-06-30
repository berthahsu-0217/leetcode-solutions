class Solution:
    def bfs(self, node, answer, graph):
        seen = set([node])
        todo = deque([node])
        depts = defaultdict(int)
        depts[node] = 0
        parents = defaultdict(int)
        parents[node] = -1
        while todo:
            cur = todo.popleft()
            for neighbor in graph[cur]:
                if neighbor not in seen:
                    todo.append(neighbor)
                    seen.add(neighbor)
                    depts[neighbor] = depts[cur] + 1
                    parents[neighbor] = cur
                elif neighbor != parents[cur]:
                    answer[0] = min(answer[0], depts[neighbor] + depts[cur] + 1)
                
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [ [] for _ in range(n) ]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        answer = [1001]
        for node in range(n):
            self.bfs(node, answer, graph)
        
        if answer[0] == 1001:
            answer[0] = -1
        
        return answer[0]
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
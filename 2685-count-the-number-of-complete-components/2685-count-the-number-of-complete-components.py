class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [set() for i in range(n)]
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        def dfs(node, paths):
            paths.add(node)
            visited.add(node)
            
            for next_node in graph[node]:
                if next_node not in visited:
                    dfs(next_node, paths)
            return

        visited = set()
        ccc = []
        for i in range(n):
            if i not in visited:
                paths = set()
                dfs(i, paths)
                ccc.append(paths)
        ans = 0
        for paths in ccc:
            completed = True
            cnt = len(paths)-1
            for node in paths:
                if len(graph[node]) != cnt:
                    completed = False
            if completed:
                ans += 1

        return ans
            
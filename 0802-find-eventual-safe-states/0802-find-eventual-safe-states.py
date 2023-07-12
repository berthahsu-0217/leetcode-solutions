class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node):
            if dp[node] is not None: #node is checked before
                return dp[node]
            if node in visited: #cycle
                return False
            visited.add(node)
            
            safe = True
            for next_node in graph[node]:
                safe &= dfs(next_node)
                
            dp[node] = safe
            return safe
            
        
        n = len(graph)
        dp = [None]*n
        visited = set()
        
        for i in range(n):
            if i not in visited:
                dfs(i)
        
        ans = [i for i, x in enumerate(dp) if x]
        return ans
        
        
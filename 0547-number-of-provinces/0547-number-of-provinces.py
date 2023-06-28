class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
        
        provinces = 0
        visited = set()
        
        n = len(isConnected)
        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1
        
        return provinces
            
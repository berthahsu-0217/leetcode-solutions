class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.n = n
        self.dist = [[float("inf") for j in range(n)] for i in range(n)]
        for i in range(n):
            self.dist[i][i] = 0
        for a, b, cost in edges:
            self.dist[a][b] = cost
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k]+self.dist[k][j])
        
    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        for i in range(self.n):
            for j in range(self.n):
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][a]+self.dist[b][j]+cost)
        
    def shortestPath(self, node1: int, node2: int) -> int:
        return -1 if self.dist[node1][node2] == float("inf") else self.dist[node1][node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
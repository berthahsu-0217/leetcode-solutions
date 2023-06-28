import heapq as hq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = [dict() for i in range(n)]
        for edge, prob in zip(edges, succProb):
            u, v = edge
            graph[u][v] = prob
            graph[v][u] = prob
        
        probs = [0]*n
        probs[start] = -1
        
        heap = []
        hq.heappush(heap, (-1, start))
        
        while heap:
            prob, node = hq.heappop(heap)
            if node == end:
                return -probs[end]
            if prob == probs[node]:
                for next_node, p in graph[node].items():
                    if prob*p < probs[next_node]:
                        probs[next_node] = prob*p
                        hq.heappush(heap, (probs[next_node], next_node))
        
        return 0
            
            
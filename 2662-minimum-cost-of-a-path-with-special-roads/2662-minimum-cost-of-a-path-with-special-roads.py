import heapq as hq
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        
        """
        graph
        start x0, y0
        target xt, yt
        specialRoads[i] = x1, y1, x2, y2, c
        Edges:
        1. all nodes to target
        2. all nodes to (x2, y2) pairs
        """
        
        x0, y0 = start
        xt, yt = target
        n = len(specialRoads)
        heap = []
        dist = {(x0, y0):0}
        hq.heappush(heap, (x0, y0, 0))
        
        while heap:
            x, y, d = hq.heappop(heap)
            if x == xt and y == yt:
                return d
            if d == dist[(x, y)]:
                #to target
                if d+abs(x-xt)+abs(y-yt) < dist.get((xt, yt), float("inf")):
                    dist[(xt, yt)] = d+abs(x-xt)+abs(y-yt)
                    hq.heappush(heap, (xt, yt, dist[xt, yt]))
                #to x2, y2
                for i in range(n):
                    x1, y1, x2, y2, c = specialRoads[i]
                    if d+abs(x-x1)+abs(y-y1)+c < dist.get((x2, y2), float("inf")):
                        dist[(x2, y2)] = d+abs(x-x1)+abs(y-y1)+c
                        hq.heappush(heap, (x2, y2, dist[(x2, y2)]))
        
        return -1
                    
        
        
        
            
            
        
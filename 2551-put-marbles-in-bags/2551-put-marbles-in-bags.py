class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
            
        n = len(weights)
        
        if n == k:
            return 0
        
        points = []
        
        for i in range(n-1):
            points.append(weights[i]+weights[i+1])
        
        points.sort()
        
        #print(points)
        #print(points[:k-1])
        #print(points[n-k:n-1])
        
        return sum(points[n-k:n-1])-sum(points[:k-1])
        
    
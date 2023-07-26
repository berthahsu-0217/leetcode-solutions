import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        """
        hour >= ceil(d1/speed)+ceil(d2/speed)+ceil(d3/speed)+...
        """
        def verify(speed):
            if speed == 0:
                return False
            h = 0
            for i in range(n-1):
                h += math.ceil(dist[i]/speed)
                if h > hour: return False
            h += dist[-1]/speed
            return h <= hour
            
        n = len(dist)
        l, r = 0, 10000001
        
        while l < r:
            m = (l+r)//2
            #print(m, verify(m))
            if verify(m):
                r = m
            else:
                l = m+1
        return -1 if l == 10000001 else l
        
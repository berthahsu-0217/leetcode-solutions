import heapq as hq

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        """
        1234
        CAKE
        
        "","" => (0,0)
        "",C  => (0,1)
        C,""  => (1,0)
        A, C  => (2,1)
        "",A  => (0,2)
        ...
        """
        
        def dist(c1, c2):
            if c1 is "":
                return 0
            i1 = ord(c1)-ord("A")
            i2 = ord(c2)-ord("A")
            x1, y1 = i1//6, i1%6
            x2, y2 = i2//6, i2%6
            return abs(x1-x2)+abs(y1-y2)
           
        n = len(word)
        #dp[i][j] = min distance to (word[i-1], word[j-1])
        dp = [[float("inf") for j in range(n+1)] for i in range(n+1)]
        dp[0][0] = 0
        heap = [(0,0,0)]
        
        min_dist = float("inf")
        
        while heap:
            d, i, j = hq.heappop(heap)
            if i == n or j == n: #reach end state
                min_dist = min(min_dist, d)
                continue
            if d != dp[i][j]: continue #if not the best distance, do not update based on this
            #traverse to the edges
            next_idx = max(i, j)+1
            #first finger to next_idx
            cost1 = d + dist(word[i-1] if i > 0 else "", word[next_idx-1])
            if cost1 < dp[next_idx][j]:
                dp[next_idx][j] = cost1
                hq.heappush(heap, (cost1, next_idx, j))
            cost2 = d + dist(word[j-1] if j > 0 else "", word[next_idx-1])
            if cost2 < dp[i][next_idx]:
                dp[i][next_idx] = cost2
                hq.heappush(heap, (cost2, i, next_idx))
        
        return min_dist
                
                
            
        
        
        
        
        
        
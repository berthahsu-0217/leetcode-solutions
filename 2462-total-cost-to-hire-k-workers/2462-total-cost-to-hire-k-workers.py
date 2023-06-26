import heapq as hq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        """
         0  1  2 3 4 5  6  7 8
                     l
        17,12,10,2,7,2,11,20,8
                   r
        first_heap (7,4),(10,2),(12,1),(17,0)
        last_heap (8,8),(11,6),(20,7)
        n 9
        k 3
        candidates 4
        total_cost 2+2
        first_min (2,3) (7,4)
        last_min  (2,5) (2,5)
        """
        n = len(costs)
        l, r = 0, n-1
        first_heap = []
        last_heap = []
        
        for i in range(candidates):
            if l <= r:
                hq.heappush(first_heap, (costs[l], l))
                l += 1
            if l <= r:
                hq.heappush(last_heap, (costs[r], r))
                r -= 1
            if l > r:
                break
        
        total_cost = 0
        for i in range(k):
            first_min = first_heap[0] if first_heap else (float("inf"),-1)
            last_min = last_heap[0] if last_heap else (float("inf"),-1)
            
            if first_min < last_min:
                hq.heappop(first_heap)
                total_cost += first_min[0]
                if l <= r:
                    hq.heappush(first_heap, (costs[l], l))
                    l += 1
            else:
                hq.heappop(last_heap)
                total_cost += last_min[0]
                if l <= r:
                    hq.heappush(last_heap, (costs[r], r))
                    r -= 1
                    
        return total_cost
            
            
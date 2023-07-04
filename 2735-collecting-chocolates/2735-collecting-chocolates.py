class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        
        """
        20,1,15
        
        (i+1)th cost + x
        
        0 1 2
        2 0 1
        1 2 0
        
        5
        1 2 4 10 5 1 10
        0 1 2 3  4 5 6
        6 0 1 2  3 4 5
        """
        
        n = len(nums)
        #cost[i][j]: minimum cost of picking jth type after ith operation 
        cost = [[float("inf") for j in range(n)] for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i-1][j], nums[(j+i)%n])
        
        #print(cost)
        
        min_cost = float("inf")
        
        for i in range(n):
            total_cost = i*x
            for j in range(n):
                total_cost += cost[i][j]
            min_cost = min(min_cost, total_cost)
        
        return min_cost
                
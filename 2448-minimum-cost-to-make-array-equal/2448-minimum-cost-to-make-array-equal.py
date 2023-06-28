class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        
        n = len(nums)
        
        num_and_cost = [(num, c) for num, c in zip(nums, cost)]
        num_and_cost.sort()
        
        prefix_cost = [0]*n
        prefix_cost[0] = num_and_cost[0][1]
        for i in range(1, n):
            prefix_cost[i] = prefix_cost[i-1]+num_and_cost[i][1]
        
        #Make elements equal to nums[0]
        total_cost = 0
        for i in range(1, n):
            total_cost += (num_and_cost[i][0]-num_and_cost[0][0])*num_and_cost[i][1]
        
        #Make elements equal to nums[i]
        ans = total_cost
        for i in range(1, n):
            gap = num_and_cost[i][0]-num_and_cost[i-1][0]
            inc = prefix_cost[i-1] #additional unit of costs for elements larger than nums[i]
            dec = prefix_cost[n-1]-prefix_cost[i-1] #redundant unit of costs for elements larger than nums[i]
            total_cost += gap*(inc-dec)
            ans = min(ans, total_cost)
        
        return ans
            
        
        
        
            
        
            
            
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        curr_max_i = next_max_i = 0
        jumps = 0
        
        for i in range(n):
            if curr_max_i < i:
                jumps += 1
                curr_max_i = next_max_i
            next_max_i = max(next_max_i, i+nums[i])
            
        return jumps
        
        
        """ O(n**2)
        def myMin(a, b):
            if a is None:
                return b
            return min(a,b)
        
        n = len(nums)
        dp = [None for i in range(n)]
        dp[0] = 0
        
        for i in range(n):
            #print(dp)
            if dp[i] is None: #if i cannot be reached
                continue
            for j in range(nums[i]+1):
                if i+j < n:
                    dp[i+j] = myMin(dp[i+j], dp[i]+1)
        
        return dp[n-1]
        """
        
                
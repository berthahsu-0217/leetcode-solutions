class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
        """
        n = 4
        
        1111
        10000-1
        01111
        
        
        0101
        
        """
        @cache
        def dfs(i, bitmask):
            if bitmask == final_state:
                return 1
            n_ways = 0
            for j in range(n):
                if (bitmask & (1 << j)) == 0 and (bitmask == 0 or nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    n_ways += dfs(j, bitmask | (1 << j))
                    n_ways %= MOD
            
            return n_ways
        
        MOD = 1000000007
        n = len(nums)
        final_state = (1 << n)-1
        
        return dfs(0, 0)
        
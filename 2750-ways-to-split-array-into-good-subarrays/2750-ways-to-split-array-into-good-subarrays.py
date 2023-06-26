class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        """
        0 1 2 3 4
        0,1,0,0,1,0,1,0
          x x x  
          
        3x2
          
        0 1 0
        0 1 
          
        3x2x
        
                i
          p
        
        l -1
        p  1
        """
        
        MOD = 1000000007
        
        n = len(nums)
        
        one = None
        
        ans = 1
        
        for i, x in enumerate(nums):
            if x == 1:
                if one is not None:
                    ans = (ans*(i-one)) % MOD
                one = i
        
        if one is None:
            return 0
        return ans
            
        
            
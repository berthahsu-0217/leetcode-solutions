class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 1
        
        i = 0
        while i < n:
            ridx = nums[i]-1
            if ridx < 0 or ridx >= n or nums[ridx] == nums[i]:
                i += 1
            else:
                nums[ridx], nums[i] = nums[i], nums[ridx]
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1
                
            
        
            
                
                    
                    
            
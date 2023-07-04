class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        
        """
        [-2,0,2]
        "RLL"
        d = 3
        
        [1,-3,-1]
        
        
        [1, 0]
        
        [3 -2]
        """
        
        MOD = 10**9+7
        
        stack = []
        
        n = len(nums)
        
        for i in range(n):
            if s[i] == "L":
                nums[i] -= d
            else:
                nums[i] += d
            
        nums.sort()
        
        ans = 0
        
        dist = 0
        for i in range(1, n):
            dist2 = dist+(nums[i]-nums[i-1])*i
            ans = (ans + dist2) % MOD
            dist = dist2
        
        return ans
            
        
        
        
            
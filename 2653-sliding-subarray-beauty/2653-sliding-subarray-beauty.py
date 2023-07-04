class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def Xth(x):
            cnt = 0
            for i in range(50, 0, -1):
                if cnt+freq[i] >= x:
                    return -i
                cnt += freq[i]
            return 0
                    
        freq = [0]*51
        ans = []
        n = len(nums)
        
        for i in range(n):
            
            if i-k >= 0 and nums[i-k] < 0:
                freq[-nums[i-k]] -= 1
            if nums[i] < 0:
                freq[-nums[i]] += 1
            if i >= k-1:
                ans.append(Xth(x))
        
        return ans
            
            
                
                
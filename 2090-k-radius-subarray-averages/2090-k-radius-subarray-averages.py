class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n
        
        s = 0
        for i in range(k, n-k):
            if i == k:
                s = sum([nums[j] for j in range(2*k+1)])
            else:
                s += nums[i+k]-nums[i-k-1]
            ans[i] = s//(2*k+1)
        
        return ans
            
                    
        
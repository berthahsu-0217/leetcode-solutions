class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        ans = 0
        max_num = 0
        i, lens = 0, len(nums)
        
        while max_num < n:
            if i < lens and nums[i] <= max_num+1:
                max_num = max_num+nums[i]
                i += 1
            else:
                max_num += max_num+1
                ans += 1
        
        return ans
            
                
            
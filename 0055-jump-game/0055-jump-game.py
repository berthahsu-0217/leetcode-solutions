class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        max_idx = 0
        for i in range(n):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i+nums[i])
        
        return True
            
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        min_i = max_i = None
        
        for i in range(n):
            if nums[i] == 1:
                min_i = i
            if nums[i] == n:
                max_i = i
        
        if min_i < max_i:
            return min_i + n-max_i-1
        return min_i+n-max_i-2
        
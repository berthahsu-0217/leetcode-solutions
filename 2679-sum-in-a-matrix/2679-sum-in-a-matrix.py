class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        m, n = len(nums), len(nums[0])
        
        for i in range(m):
            nums[i] = sorted(nums[i])
        
        score = 0
        for j in range(n):
            max_val = -1
            for i in range(m):
                max_val = max(max_val, nums[i][j])
            score += max_val
        
        return score
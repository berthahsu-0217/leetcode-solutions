class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        MIN = min(nums)
        MAX = max(nums)
        
        for x in nums:
            if x != MIN and x != MAX:
                return x
        
        return -1
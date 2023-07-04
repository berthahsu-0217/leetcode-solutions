class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        x = max(nums)
        
        return k*(x+x+k-1)//2
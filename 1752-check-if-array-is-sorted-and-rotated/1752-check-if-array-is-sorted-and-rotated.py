class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)
        reversed = False
        
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if reversed:
                    return False
                reversed = True
                
        return not reversed or nums[-1] <= nums[0]
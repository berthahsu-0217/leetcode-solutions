class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                nums[k] = nums[i]
                k += 1
        
        return k
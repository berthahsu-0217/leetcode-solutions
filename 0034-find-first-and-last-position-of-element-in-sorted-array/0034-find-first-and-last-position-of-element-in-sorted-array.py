class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst(nums, target):
            n = len(nums)
            l, r = 0, n
            while l < r:
                m = l+(r-l)//2
                if nums[m] < target:
                    l = m+1
                else:
                    r = m
            return l
            
        def findLast(nums, target):
            n = len(nums)
            l, r = 0, n
            while l < r:
                m = l+(r-l)//2
                if nums[m] <= target:
                    l = m+1
                else:
                    r = m
            return l
        
        n = len(nums)
        idx1 = findFirst(nums, target)
        idx2 = findLast(nums, target)
        if idx1 == idx2:
            return [-1,-1]
        return [idx1, idx2-1]
                    
                
                
    
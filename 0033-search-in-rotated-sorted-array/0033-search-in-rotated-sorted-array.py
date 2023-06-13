class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l, r = 0, n
        
        while l < r:
            m = l+(r-l)//2
            #case1
            if nums[m] == target:
                return m
            #case2: piovt on right
            if nums[l] < nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m
                else:
                    r = m
            #case3: pivot of left
            else:
                if target < nums[m] or target > nums[r-1]:
                    r = m
                else:
                    l = m
                    
        return -1
                
            
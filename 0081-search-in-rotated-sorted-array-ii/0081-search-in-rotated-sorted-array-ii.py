class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        
        l, r = 0, n
        
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            #cannot decide mid on F or S
            if nums[l] == nums[m]:
                l += 1
                continue
            #on different sides
            #m on F, target on S
            elif nums[l] < nums[m] and target < nums[l]:
                l = m+1
            #m on S, target on F
            elif nums[l] > nums[m] and target >= nums[l]:
                r = m
            #on same sides
            else:
                if nums[m] < target:
                    l = m+1
                else:
                    r = m
                    
        return False
                
            
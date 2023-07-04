class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        
        return self.solution1(nums)
    
    #O(n^2)
    def solution1(self, nums):
        
        n = len(nums)
        ans = 0
        
        for i in range(n):
            vals = set()
            imbalances = 0
            for j in range(i, n):
                #nums[j] is already in the set, does not create any more gap
                if nums[j] in vals:
                    pass
                #original gap: nums[j-1], nums[j+1] => by adding nums[j] the gap is gone
                elif (nums[j]-1 in vals) and (nums[j]+1 in vals):
                    imbalances -= 1
                #if vals already has some elements, adding nums[j] will add an additional gap
                elif (nums[j]-1 not in vals) and (nums[j]+1 not in vals) and vals:
                    imbalances += 1
                vals.add(nums[j])
                ans += imbalances
        
        return ans
    
    
                    
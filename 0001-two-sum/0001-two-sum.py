class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val_to_idx = dict()
        
        for i, x in enumerate(nums):
            if target-x in val_to_idx:
                return [val_to_idx[target-x], i]
            val_to_idx[x] = i
        
        return [-1,-1]
from collections import Counter
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = set()
        suffix = dict()
        for x in nums:
            suffix[x] = suffix.get(x,0)+1
        
        diff = [None]*n
        
        for i in range(n):
            prefix.add(nums[i])
            suffix[nums[i]] -= 1
            if suffix[nums[i]] == 0:
                del suffix[nums[i]]
            diff[i] = len(prefix)-len(suffix)
        
        return diff
            
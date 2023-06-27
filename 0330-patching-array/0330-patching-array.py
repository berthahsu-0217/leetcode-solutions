class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        """
        [1,3]
        
        Each time adding an extra element nums[i], check to see if max_sum+1 can be reached
        if not: pad max_sum+1 to array => max_num += max_num+1
        if can: i += 1
        """
        pads = 0
        max_num = 0
        i, lens = 0, len(nums)
        
        while max_num < n:
            if i < lens and nums[i] <= max_num+1:
                max_num = max_num+nums[i]
                i += 1
            else:
                max_num += max_num+1
                pads += 1  #pad max_num+1
                
        return pads
            
                
            
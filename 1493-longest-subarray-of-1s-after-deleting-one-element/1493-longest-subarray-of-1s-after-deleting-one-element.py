class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_lens = 0
        ones1 = ones2 = 0
        zero = False
        
        for x in nums:
            if x == 0:
                max_lens = max(max_lens, ones1+ones2)
                ones1, ones2 = ones2, 0
                zero = True
            else:
                ones2 += 1
        max_lens = max(max_lens, ones1+ones2)
        
        if not zero:
            max_lens -= 1
        
        return max_lens
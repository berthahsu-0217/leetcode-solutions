class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_lens = float("inf")
        l = r = 0
        n = len(nums)
        
        s = 0
        while r < n:
            s += nums[r]
            while l <= r and s >= target:
                min_lens = min(min_lens, r-l+1)
                s -= nums[l]
                l += 1
            r += 1
        
        if min_lens == float("inf"):
            return 0
        return min_lens
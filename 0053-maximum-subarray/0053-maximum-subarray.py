class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = None
        s = 0
        for x in nums:
            s += x
            if ans is None or s > ans: ans = s
            if s < 0: s = 0
        return ans
        
        """
        n = len(nums)
        #dp[i]: maximum subarray length including i
        dp = [nums[i] for i in range(n)]
        
        for i in range(1, n):
            if dp[i-1] > 0:
                dp[i] += dp[i-1]
        return max(dp)
        """
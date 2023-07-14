class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        
        max_lens = 0
        dp = dict()
        
        for x in arr:
            if x-diff in dp:
                dp[x] = dp[x-diff]+1
            else:
                dp[x] = 1
            max_lens = max(max_lens, dp[x])
            
        return max_lens
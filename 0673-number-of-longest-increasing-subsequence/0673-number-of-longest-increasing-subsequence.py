class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        #dp[i]: [lis ending in nums[i], freq]
        dp = [[1,1] for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0]+1 > dp[i][0]:
                        dp[i] = [dp[j][0]+1, dp[j][1]]
                    elif dp[j][0]+1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        
        #print(dp)
        
        max_lis, ans = 0, 0
        for i in range(n):
            if dp[i][0] > max_lis:
                ans = dp[i][1]
                max_lis = dp[i][0]
            elif dp[i][0] == max_lis:
                ans += dp[i][1]
        
        return ans
        
        
                    
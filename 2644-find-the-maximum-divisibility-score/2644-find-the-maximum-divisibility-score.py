class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        m, n = len(nums), len(divisors)
        
        max_score = -1
        max_div = 0
        for j in range(n):
            cnt = 0
            for i in range(m):
                if nums[i] % divisors[j] == 0:
                    cnt += 1
            if max_score < cnt or (max_score == cnt and divisors[j] < max_div):
                max_div = divisors[j]
                max_score = cnt

          
        return max_div
        
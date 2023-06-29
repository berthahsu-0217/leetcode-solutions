class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        """
        Conditions:
        1. at the end, right = left
        2. right and left at most steps//2
        3. at any time, right-left = idx between [0, arrLen-1]
        """
        return self.solution2(steps, arrLen)
    #O(500*250*250) => TLE
    def solution1(self, steps, arrLen):
        
        def check(r, l, moves):
            return (r <= MAX) and (l <= MAX) and (0 <= r-l < arrLen) and (r-l <= moves)
        
        MOD = 1000000007
        MAX = steps//2
        #dp[(i,j)]: right=i times, left=j times
        dp = {(0,0):1}
        
        for i in range(1, steps+1):
            dp2 = dict()
            for r, l in dp.keys():
                #right
                if check(r+1, l, steps-i):
                    dp2[(r+1,l)] = ( dp2.get((r+1,l),0)+dp[(r,l)] ) % MOD
                #left
                if check(r, l+1, steps-i):
                    dp2[(r,l+1)] = ( dp2.get((r,l+1),0)+dp[(r,l)] ) % MOD
                #stay
                dp2[(r,l)] = ( dp2.get((r,l),0)+dp[(r,l)] ) % MOD
            dp = dp2
            
        ans = 0
        for r, l in dp.keys():
            if r == l:
                ans = ( ans+dp[(r,l)] ) % MOD
                
        return ans
    
    def solution2(self, steps, arrLen):
        
        MOD = 1000000007
        n = min(arrLen, steps//2+1)
        
        @cache
        def backtrack(i, remains):
            if remains == 0:
                return int(i == 0)
            cnt = 0
            #right
            if 0 <= i+1 < n:
                cnt = (cnt+backtrack(i+1, remains-1)) % MOD
            #left
            if 0 <= i-1 < n:
                cnt = (cnt+backtrack(i-1, remains-1)) % MOD
            #stay
            cnt = (cnt+backtrack(i, remains-1)) % MOD
            return cnt
        
        return backtrack(0, steps)
            
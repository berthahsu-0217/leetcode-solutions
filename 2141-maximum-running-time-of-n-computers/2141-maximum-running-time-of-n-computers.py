class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        l, r = 1, sum(batteries)//n+1
        
        while l < r:
            m = (l+r)//2
            extra = 0
            for power in batteries:
                extra += min(power, m)
            if extra//n >= m:
                l = m+1
            else:
                r = m
        
        return l-1
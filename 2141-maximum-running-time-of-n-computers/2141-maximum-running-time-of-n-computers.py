class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        l, r = 1, sum(batteries)//n
        
        while l < r:
            m = r-(r-l)//2
            extra = 0
            for power in batteries:
                extra += min(power, m)
            if extra//n >= m:
                l = m
            else:
                r = m-1
        
        return l
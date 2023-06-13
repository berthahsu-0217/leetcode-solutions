class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX = 2**31
        neg = (dividend < 0) ^ (divisor < 0)
        x, y = abs(dividend), abs(divisor)
        
        vals = []
        while x >= y:
            vals.append(y)
            y *= 2
        
        n = len(vals)
        if n == 0:
            return 0
        
        quo = 0
        q = 2**(n-1)
        
        for i in range(n-1,-1,-1):
            if x >= vals[i]:
                x -= vals[i]
                quo += q
            q >>= 1
            
        if neg:
            quo *= -1
            
        if (quo > MAX-1) or (quo < -MAX):
            return MAX-1
        
        return quo
        
        
        

            
            
            
        
            
            
        
        
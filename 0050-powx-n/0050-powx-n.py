class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calc(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            a = calc(x, n//2)
            if n % 2 == 1:
                return a*a*x
            else:
                return a*a
        
        neg = n < 0
        n = abs(n)
        
        res = calc(x, n)
        if neg:
            return 1/res
        return res
        
        
        
        
        
        
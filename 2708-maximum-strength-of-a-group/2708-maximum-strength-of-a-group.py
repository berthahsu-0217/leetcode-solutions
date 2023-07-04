class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        pos = []
        neg = []
        zero = False
        
        for x in nums:
            if x > 0:
                pos.append(x)
            elif x < 0:
                neg.append(x)
            else:
                zero = True
                
        product = None
        for x in pos:
            if product is None:
                product = 1
            product *= x
        
        neg.sort()
        n = len(neg)
        if n % 2 == 1:
            n -= 1
        for i in range(n):
            if product is None:
                product = 1
            product *= neg[i]
            
        if product is None:
            if zero:
                return 0
            else:
                return neg[-1]
        
        return product
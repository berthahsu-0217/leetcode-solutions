class Solution:
    def minimumOperations(self, num: str) -> int:
        
        """
        divisible by 25: (00,50), (25,75)
        """
        zero = five = False
        n = len(num)
        
        for i in range(n-1,-1,-1):
            d = int(num[i])
            if (zero and d in (0,5)) or (five and d in (2,7)):
                return n-i-2
            if d == 0: zero = True
            if d == 5: five = True
                
        return n-1 if zero else n
            
                
                
        
            
        
        
                
        
        
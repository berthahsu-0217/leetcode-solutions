class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        """
        Breaking down the question
        1.
        num1 - k*num2 - (2^i1+2^i2+...2^ik) = 0
        => target = num1 - k*num2 = (2^i1+2^i2+...2^ik) > 0 ........ (1st condition: target > 0)
        
        2.
        What are possible k for target
        Suppose target is 8 = 1000
        => 1+1+1+1+1+1+1+1 k = 8
        => 1+1+1+1+1+1+2   k = 7
        => 1+1+1+1+2+2     k = 6
        => 1+1+1+1+4       k = 5
        => 1+1+2+4         k = 4
        => 2+2+4           k = 3
        => 4+4             k = 2
        => 8               k = 1
        
        => number of 1 bits in target <= k <= target
        => (num1 - k*num2).bit_count() <= k <= (num1 - k*num2) ....... (2nd condition: target.bit_count() <= k <= target)
        
        3. Keep increasing k until it satisfies the 1st and 2nd conditions, but when should we stop?
        if target.bit_count() <= k => target 
        """
        
        target = num1
        
        k = 0
        while target > 0:
            target -= num2
            k += 1
            if target.bit_count() <= k <= target:
                return k
                
        return -1
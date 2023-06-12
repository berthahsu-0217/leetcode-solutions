class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        val = 0
        old = x
        
        while x > 0:
            d = x%10
            x //= 10
            val = val*10+d
            
            
        return val == old
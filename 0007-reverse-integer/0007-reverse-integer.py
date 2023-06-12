import sys

class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x > 0:
            d, x = x%10, x//10
            if rev > INT_MAX//10:
                return 0
            if rev == INT_MAX//10:
                if (sign < 0 and d > 8) or (sign > 0 and d > 7):
                    return 0
            rev = rev*10+d
        
        return sign*rev
        
            
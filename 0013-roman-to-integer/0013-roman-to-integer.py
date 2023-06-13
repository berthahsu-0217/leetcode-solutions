class Solution:
    def romanToInt(self, s: str) -> int:
        
        res = 0
        roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in range(len(s)):
            if i > 0 and roman_to_int[s[i-1]] < roman_to_int[s[i]]:
                res -= 2*roman_to_int[s[i-1]]
            res += roman_to_int[s[i]]
            
        return res
                
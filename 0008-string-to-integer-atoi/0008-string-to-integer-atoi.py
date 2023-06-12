class Solution:
    def myAtoi(self, s: str) -> int:
        
        def safe_calc(val, d, INT_MAX, sign):
            if val > INT_MAX//10:
                return True, INT_MAX if sign > 0 else sign*INT_MAX-1
            elif val == INT_MAX//10:
                if sign > 0 and d > 7:
                    return True, INT_MAX
                elif sign < 0 and d > 8:
                    return True, sign*INT_MAX-1
            return False, 10*val+d
            
        INT_MAX = 2147483647
        sign = 1
        val = 0
        i, n = 0, len(s)
        while i < n and s[i] == " ":
            i += 1
        if i < n and s[i] in ("+", "-"):
            if s[i] == "-": sign *= -1
            i += 1
        while i < n and s[i].isdigit():
            overflow, val = safe_calc(val, int(s[i]), INT_MAX, sign)
            if overflow: return val
            i += 1
        
        return val*sign
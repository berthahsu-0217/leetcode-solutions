class Solution:
    def isNumber(self, s: str) -> bool:
        
        def isInt(start, n):
            
            if start < n and s[start] in ("+","-"):
                start += 1
            
            #no more chars
            if start >= n:
                return False
            
            for i in range(start, n):
                if not s[i].isdigit():
                    return False
            return True
        
        
        def isDecimal(start, n):
            
            if start < n and s[start] in ("+", "-"):
                start += 1
            
            has_decimal = False
            d_before_decimal = False
            d_after_decimal = False
            
            for i in range(start, n):
                if s[i].isdigit():
                    if has_decimal:
                        d_after_decimal = True
                    else:
                        d_before_decimal = True
                elif s[i] == ".":
                    if has_decimal:
                        return False
                    has_decimal = True
                elif s[i] in ("e", "E"):
                    if not isInt(i+1, n):
                        return False
                    break
                else:
                    return False
                
            if has_decimal:
                return d_before_decimal or d_after_decimal
            return d_before_decimal
        
        #if not ans:
            #print(s)
        return isDecimal(0, len(s))
                
            
            
            
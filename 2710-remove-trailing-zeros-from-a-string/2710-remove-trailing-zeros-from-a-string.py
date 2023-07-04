class Solution:
    def removeTrailingZeros(self, s: str) -> str:
        
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] != "0":
                break
        
        return s[:i+1]
            
        
        
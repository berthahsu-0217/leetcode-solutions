class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        return self.RollingHash(haystack, needle)
        #return self.KMP(haystack, needle)
    
    def RollingHash(self, s, p):
        
        m, n = len(s), len(p)
        if m < n:
            return -1
        
        x = 3
        M = 10**9+7
        h = h_p = 0
        x_to_n = x**n
        
        for i in range(m):
            if i < n:
                h_p = ( h_p*x+ord(p[i]) )%M
                h = ( h*x+ord(s[i]) )%M
            if i >= n-1:
                if i >= n:
                    h = ( h*x+ord(s[i])-ord(s[i-n])*x_to_n )%M
                if h == h_p:
                    return i-n+1
        return -1
        
    def KMP(self, s, p):
        
        def LPS(p):
            n = len(p)
            lps = [None]*n
            lps[0] = 0
            i, j = 0, 1
            
            while j < n:
                if p[i] == p[j]:
                    i += 1
                    lps[j] = i
                    j += 1
                elif i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i-1]
            
            return lps
        
        lps = LPS(p)
        i = j = 0
        m, n = len(s), len(p)
        
        while i < m and j < n:
            if s[i] == p[j]:
                i += 1
                j += 1
                if j >= n:
                    return i-n
            elif j > 0:
                j = lps[j-1]
            else:
                i += 1
        
        return -1
        
                
            
            
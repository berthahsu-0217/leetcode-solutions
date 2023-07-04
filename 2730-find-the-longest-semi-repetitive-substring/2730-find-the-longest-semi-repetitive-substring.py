class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        n = len(s)
        l = r = 0
        
        ans = 0
        cons = False
        idx = None
        
        while r < n:
            if r-1 >= 0 and s[r-1] == s[r]:
                if cons:
                    l = idx
                    idx = r
                else:
                    cons = True
                    idx = r
            ans = max(ans, r-l+1)
            r += 1
            
        return ans
            
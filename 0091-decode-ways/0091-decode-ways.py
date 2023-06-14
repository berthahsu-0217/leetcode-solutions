class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [None for i in range(n)]
        return self.decode(0, len(s), s, dp)
    
    def decode(self, idx, n, s, dp):
        
        if idx >= n:
            return 1
        
        if dp[idx] is not None:
            return dp[idx]
        
        n_ways = 0
        
        d = int(s[idx])
        
        #one digit
        if d == 0:
            return 0
        n_ways += self.decode(idx+1, n, s, dp)
        
        #two digits
        if d <= 2 and idx+1 < n:
            if d == 1:
                n_ways += self.decode(idx+2, n, s, dp)
            elif int(s[idx+1]) <= 6:
                n_ways += self.decode(idx+2, n, s, dp)
                
        dp[idx] = n_ways
                
        return n_ways
                
        
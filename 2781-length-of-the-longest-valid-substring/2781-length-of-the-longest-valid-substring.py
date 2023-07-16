class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        x = 3
        MOD = 1000000007
        
        def hash(s):
            #print(s)
            h_prev = 0
            for c in s:
                h_prev = (h_prev*x+ord(c)) % MOD
            #print(s, h_prev)
            return h_prev
        
        #print(hash("aa"), hash("aaa"))
        
        forbidden = set([hash(s) for s in forbidden])
        #print(forbidden)
        #print(forbidden)
        n = len(word)
        min_r = [n]*n

        for i in range(n):
            h_prev = 0
            for j in range(10):
                if i+j >= n: break
                h_prev = (h_prev*x+ord(word[i+j])) % MOD
                #print(i, h_prev)
                if h_prev in forbidden:
                    #print(i, j, h_prev)
                    min_r[i] = min(min_r[i], i+j)
        
        ans = 0
        r = n
        for i in range(n-1,-1,-1):
            r = min(r, min_r[i])
            ans = max(ans, r-i)
            
        return ans
        
            
                
                
        
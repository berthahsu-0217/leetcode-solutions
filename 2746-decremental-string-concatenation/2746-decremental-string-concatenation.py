class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        
        n = len(words)
        dp = dict()
        first, last = words[0][0], words[0][-1]
        #print(first, last)
        dp[(ord(first)-ord("a"), ord(last)-ord("a"))] = len(words[0])
        #print(dp[ord(first)-ord("a")][ord(last)-ord("a")])
        
        for t in range(1, n):
            dp2 = dict()
            first, last = words[t][0], words[t][-1]
            #print(first, last)
            ii, jj = ord(first)-ord("a"), ord(last)-ord("a")
            
            for i, j in dp:
                #str, word
                dp2[(i, jj)]= min( dp2.get((i, jj), float("inf")), dp[(i,j)]+len(words[t])-(j == ii) )
                dp2[(ii, j)] = min( dp2.get((ii, j), float("inf")), dp[(i,j)]+len(words[t])-(jj == i) )
            
            dp = dp2
        
        #print(dp)
        ans = float("inf")
        for i, j in dp:
            ans = min(ans, dp[(i,j)])
        
        return ans
                
            
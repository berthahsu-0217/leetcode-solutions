class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        states = [""]
        for i in range(n):
            states.append(p[i])
        n += 1
        dp = [False for i in range(n)]
        dp[0] = True #set initial state to True
        
        #take no char, state i to state i+1
        for i in range(n-1):
            if dp[i] and states[i+1] == "*":
                dp[i+1] = True
        
        for j in range(m):
            dp2 = [False for i in range(n)]
            for i in range(n):
                #take one char, state i to state i+1
                if dp[i] and i+1 < n and states[i+1] in (s[j], "?", "*"):
                    dp2[i+1] = True
                #take one char, stay at state i
                if dp[i] and states[i] == "*":
                    dp2[i] = True
            #take no char, state i to state i+1
            for i in range(n-1):
                if dp2[i] and states[i+1] == "*":
                    dp2[i+1] = True
            dp = dp2
            
        return dp[n-1]
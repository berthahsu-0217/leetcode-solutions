class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        #states: initial, intermediate, final states
        #(char, 0 or more?) represents the conditions to match each state
        states = [('', False)] #initial state
        t = 0
        while t < len(p):
            if t+1 < len(p) and p[t+1] == '*':
                states.append((p[t], True))
                t += 1
            else:
                states.append((p[t], False))
            t += 1
        #print(states)
        
        m, n = len(s), len(states)
        
        #record whether each state is possible
        dp = [False]*n #at current step
        dp[0] = True #set initial state to True
        dp2 = [False]*n #at the next step
        
        #take no char, move to next state, given current state is True
        for j in range(n):
            if j+1 < n and dp[j] and states[j+1][1]:
                dp[j+1] = True
                
        for i in range(m):
            for j in range(n):
                #take s[i], stay at this state
                if dp[j] and states[j][1] and states[j][0] in (s[i], '.'):
                    dp2[j] = True
                #take s[i], move to next state
                if j+1 < n and dp[j] and states[j+1][0] in (s[i], '.'):
                    dp2[j+1] = True
            tmp = dp
            dp = dp2
            dp2 = tmp
            #take no char, move to next state
            for j in range(n):
                if j+1 < n and dp[j] and states[j+1][1]:
                    dp[j+1] = True
                dp2[j] = False #clean dp2
        
        return dp[n-1]
        
                
        
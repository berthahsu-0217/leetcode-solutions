class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dictionary = set([s for s in dictionary])
        
        #print(dictionary)
        
        n = len(s)
        is_word = [[False for j in range(n+1)] for i in range(n)]
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] in dictionary:
                    #print(s[i:j])
                    is_word[i][j] = True
        
        #print(is_word)
        dp = [0]*(n+1)
        
        """
        dp[0] = 0
        
        dp[j] = s[0:j]
        """
        
        #print(is_word)
        
        for i in range(1, n+1):
            for j in range(i):
                if is_word[j][i]:
                    dp[i] = max(dp[i], dp[j]+(i-j))
                else:
                    dp[i] = max(dp[i], dp[j])
                    
        #print(dp)
        
        return n-max(dp)
        
        
        
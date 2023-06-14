class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        """
        s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        s1,s2,s3
        0,0,0
        1,0,1
        2,0,2
        2,1,3
        3,1,4   2,2,4
        3,2,5   3,2,5   2,3,5
        """
        
        m = len(s1)
        n = len(s2)
        
        dp = [[None for j in range(n+1)] for i in range(m+1)]
        
        return self.recurse(s1,s2,s3,0,0,0,dp)
        
    def recurse(self, s1, s2, s3, idx1, idx2, idx3, dp):
        
        if idx3 >= len(s3):
            return idx1 >= len(s1) and idx2 >= len(s2)
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]
        
        if idx1 < len(s1) and s3[idx3] == s1[idx1]:
            check = self.recurse(s1,s2,s3,idx1+1,idx2,idx3+1,dp)
            if check:
                dp[idx1][idx2] = True
                return True
        
        if idx2 < len(s2) and s3[idx3] == s2[idx2]:
            check = self.recurse(s1,s2,s3,idx1,idx2+1,idx3+1,dp)
            if check:
                dp[idx1][idx2] = True
                return True
            
        dp[idx1][idx2] = False
        return False
            
        
        
        
        
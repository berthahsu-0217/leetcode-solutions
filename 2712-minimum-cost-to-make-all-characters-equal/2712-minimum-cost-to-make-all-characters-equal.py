class Solution:
    def minimumCost(self, s: str) -> int:
        
        n = len(s)
        
        cost = 0
        for i in range(n):
            if i > 0 and s[i] != s[i-1]:
                cost += min(i, n-i)
        
        return cost
       
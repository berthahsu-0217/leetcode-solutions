import math

MAX = 1000000
prime = [True]*(MAX+1)
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(MAX))+1):
    if prime[i]:
        for j in range(2*i, MAX+1, i):
            prime[j] = False

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        ans = []
        
        for i in range(1, n//2+1):
            if prime[i] and prime[n-i]:
                ans.append([i, n-i])
        
        return ans
            
            
                
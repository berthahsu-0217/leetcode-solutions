def partition(s, target):
    
    def go(i, n, val):
        
        #print(i, n, val)
    
        if i >= n:
            return val == target
        
        for j in range(i+1, n+1):
            if int(s[i:j])+val <= target:
                if go(j, n, int(s[i:j])+val):
                    return True
        
        return False
    
    return go(0, len(s), 0)


arr = [False]*1001

for i in range(1, 1001):
    if partition(str(i*i), i):
        arr[i] = True
        
prefix = [0]*1001

for i in range(1, 1001):
    prefix[i] += prefix[i-1]
    if arr[i]:
        prefix[i] += i*i

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        #print(arr)
        return prefix[n]
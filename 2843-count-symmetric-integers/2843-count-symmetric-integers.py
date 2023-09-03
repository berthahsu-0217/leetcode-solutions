class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        ans = 0
        
        for i in range(low, high+1):
            s = str(i)
            if len(s) == 2 and int(s[0])==int(s[1]):
                ans += 1
            if len(s) == 4 and int(s[0])+int(s[1])==int(s[2])+int(s[3]):
                ans += 1
        
        return ans
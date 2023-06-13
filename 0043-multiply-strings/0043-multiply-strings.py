class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        m, n = len(num1), len(num2)
        
        ans = 0
        mul1 = 1
        for i in range(m-1,-1,-1):
            val, mul2 = 0, 1
            for j in range(n-1, -1, -1):
                val += int(num1[i])*int(num2[j])*mul2
                mul2 *= 10
            ans += val*mul1
            mul1 *= 10
            
        return str(ans)
                
        
        
        
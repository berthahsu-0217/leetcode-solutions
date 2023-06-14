class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        arr = []
        
        m, n = len(a), len(b)
        i, j = m-1, n-1
        
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            s = carry
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            carry, d = s//2, s%2
            arr.append(str(d))
            
        return "".join(arr[::-1])
            
        
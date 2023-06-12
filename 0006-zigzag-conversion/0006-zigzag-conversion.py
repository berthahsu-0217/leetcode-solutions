class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        arr = [[] for x in range(numRows)]
        
        x, dx = 0, 1
        sign = -1
        
        for i in range(len(s)):
            arr[x].append(s[i])
            if x+dx == -1 or x+dx == numRows:
                dx *= sign
            x = (x+dx)%numRows
        
        return "".join(["".join(x) for x in arr])
                
            
        
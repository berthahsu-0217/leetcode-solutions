class Solution:
    def smallestString(self, s: str) -> str:
        
        arr = [c for c in s]
        
        n = len(arr)
        
        changed = False
        for i in range(n):
            if arr[i] == "a":
                if changed: break
            else:
                arr[i] = chr(ord(arr[i])-1)
                changed = True
                
        if not changed:
            arr[-1] = "z"
        
        return "".join(arr)
                
            
                    
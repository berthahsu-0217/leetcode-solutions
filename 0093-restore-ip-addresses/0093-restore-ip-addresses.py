class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        
        def backtrack(i, n, val, arr, dots):
            
            if i >= n or dots > 3: #end of s or too many dots
                if dots == 3:
                    ans.append("".join(arr))
                return
            
            #add dot
            if val is not None:
                arr.append('.')
                backtrack(i, n, None, arr, dots+1)
                arr.pop()
                
            #add digit
            d = int(s[i])
            if val is None or (val != 0 and 10*val+d <= 255):
                arr.append(s[i])
                backtrack(i+1, n, 10*int(val or 0)+d, arr, dots)
                arr.pop()
            
        backtrack(0, len(s), None, [], 0)
        return ans
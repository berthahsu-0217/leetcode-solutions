class Solution:
    def addMinimum(self, word: str) -> int:
        
        n = len(word)
        
        s = "abc"
        
        ans = 0

        i = 0
        idx = 0
        
        while i < n:
            if word[i:i+3] == "abc":
                i += 3
            elif word[i:i+2] in ("ab", "ac", "bc"):
                i += 2
                ans += 1
            else:
                i += 1
                ans += 2
        
        return ans
                
            
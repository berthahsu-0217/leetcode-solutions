from collections import Counter
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        n = len(s)
        
        counter = Counter([c for c in s])
        
        for f in counter.values():
            while f >= 3:
                n -= 2
                f -= 2
            if f == 2:
                n -= 1
                f -= 1
        
        return n
            
        
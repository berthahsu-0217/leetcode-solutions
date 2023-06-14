class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        def scramble(s, target):
            
            n = len(s)
            same = (s == target)
            if n == 1 or same:
                return same
            if (s, target) in dp:
                return dp[(s, target)]
            
            for j in range(1, n):
                x, y = s[:j], s[j:]
                #keep
                if scramble(x, target[:j]) and scramble(y, target[j:]):
                    dp[(s, target)] = True
                    return True
                #swap
                if scramble(x, target[n-j:]) and scramble(y, target[:n-j]):
                    dp[(s, target)] = True
                    return True
            
            dp[(s, target)] = False
            return False
        
        dp = dict()
        return scramble(s1, s2)
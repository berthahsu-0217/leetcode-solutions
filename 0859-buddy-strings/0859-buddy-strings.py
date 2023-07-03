class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        """
        1. len(s) == len(goal)
        2. 2 pairs of diff chars btw s and goal => s[i1] = goal[i2], s[i2] = goal[i1]
        3. >= 2 same chars in s
        """
        if len(s) != len(goal):
            return False
        
        n = len(s)
        chars = [0]*26
        i1 = i2 = None
        
        for i in range(n):
            if s[i] != goal[i]:
                if i1 is None:
                    i1 = i
                elif i2 is None:
                    i2 = i
                else:
                    return False #>2 diff
            chars[ord(s[i])-ord("a")] += 1
            
        if i1 == i2 == None:
            for c in range(26):
                if chars[c] >= 2:
                    return True
            return False
        elif i1 is None or i2 is None:
            return False
        
        return s[i1] == goal[i2] and s[i2] == goal[i1]
                
        
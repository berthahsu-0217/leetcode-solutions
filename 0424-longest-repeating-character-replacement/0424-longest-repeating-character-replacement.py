class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        1. Each change to the same letter, 26 options to choose
        2. Only change those that are not the letter
        3. If there is a substring of length l, there must be a substring of length l-1 => monotonic => binary search
        4. Binary search range [1,n], for each l, check if it is valid
        5. Check using sliding window of l, quickly get the number using prefix_sum to be changed is less than k
        """
        
        def verify(l):
            for i in range(l-1, n):
                for j in range(26):
                    required = prefix_letters[j][i]
                    if i-l >= 0:
                        required -= prefix_letters[j][i-l]
                    if required <= k:
                        return True
            return False
        
        n = len(s)
        #prefix_letters[j][i]: number of letters that are not chr(j+ord("A")) in substring[0:i+1]
        prefix_letters = [[0]*n for j in range(26)]
        
        for i in range(n):
            idx = ord(s[i])-ord("A")
            for j in range(26):
                prefix_letters[j][i] += int(j != idx)
                if i > 0:
                    prefix_letters[j][i] += prefix_letters[j][i-1]
                    
        l, r = 1, n+1
        
        while l < r:
            m = (l+r)//2
            if verify(m):
                l = m+1
            else:
                r = m
                
        return l-1
        
        
                
        
        
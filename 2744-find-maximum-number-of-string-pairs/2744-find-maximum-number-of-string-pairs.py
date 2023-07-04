class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        def reverse(s):
            s = [c for c in s]
            return "".join(s[::-1])
        
        ans = 0
        
        n = len(words)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if words[i] == reverse(words[j]):
                    ans += 1
        
        return ans
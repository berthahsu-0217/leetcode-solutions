from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        m, n = len(s), len(t)
        counterT = Counter(t)
        counterS = Counter()
        verified = 0
        
        ans = [float("inf"), -1, -1]
        min_lens = m
        l = r = 0
        while r < m:
            if s[r] in counterT:
                counterS[s[r]] += 1
                if counterS[s[r]] == counterT[s[r]]:
                    verified += 1
            while l <= r and verified == len(counterT):
                if r-l+1 < ans[0]:
                    ans[0] = r-l+1
                    ans[1], ans[2] = l, r
                if s[l] in counterT:
                    counterS[s[l]] -= 1
                    if counterS[s[l]] < counterT[s[l]]:
                        verified -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2]+1]
                
        
        
            
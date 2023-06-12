class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(l, r):
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return [l+1,r]
        
        def myMax(l, r, ans):
            if r-l > ans[1]-ans[0]:
                return [l,r]
            return ans
        
        ans = [-1,-1]
        n = len(s)
        
        for i in range(n):
            ll, rr = expand(i, i)
            ans = myMax(ll, rr, ans)
            ll, rr = expand(i,i+1)
            ans = myMax(ll, rr, ans)
        
        return s[ans[0]:ans[1]]
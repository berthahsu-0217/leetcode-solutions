class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        """
        k <= len(cookies) => each child receives at least one bag of cookies
        early stopping: compare number of children without cookies and the remaining bags to distribute to
        """
        
        def backtrack(i, n, no_cookies):
            nonlocal ans
            
            if (n-i) < no_cookies:
                return
            if i >= n:
                if no_cookies == 0:
                    ans = min(ans, max(children))
                return
            
            for j in range(k):
                flag = (children[j] == 0)
                children[j] += cookies[i]
                backtrack(i+1, n, no_cookies-int(flag))
                children[j] -= cookies[i]
                
        
        ans = float("inf")
        children = [0]*k
        backtrack(0, len(cookies), k)
        
        return ans
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        """
        k <= len(cookies) => each child receives at least one bag of cookies (the pigeonhole principle)
        early stopping: compare number of children without cookies and the remaining bags to distribute to
        """
        
        def backtrack(i, n, no_cookies):
            nonlocal ans
            
            #early stopping
            if (n-i) < no_cookies: #if number of children without cookies are greater than the remaining bags
                return
            
            #base case
            if i >= n:
                if no_cookies == 0:
                    ans = min(ans, max(children))
                return
            
            for j in range(k):
                x = int(children[j] == 0)
                children[j] += cookies[i]
                backtrack(i+1, n, no_cookies-x)
                children[j] -= cookies[i]
        
        ans = float("inf")
        children = [0]*k
        backtrack(0, len(cookies), k)
        
        return ans
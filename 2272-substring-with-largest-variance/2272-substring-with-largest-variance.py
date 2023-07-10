class Solution:
    def largestVariance(self, s: str) -> int:
        
        """
        aababbb
        [1,1,-1,1,-1,-1,-1]
        
        -1 1 -1
        
        """
        def maxVar(c1, c2):
            
            cnt1 = 0
            cnt2 = None
            max_var = None
            flag1 = flag2 = False
            
            for c in s:
                if c == c1:
                    cnt1 += 1
                    if cnt2 is not None:
                        cnt2 += 1
                    flag1 = True
                if c == c2:
                    cnt2 = -1
                    cnt1 -= 1
                    flag2 = True
            
                if flag1 and flag2 and (max_var is None or cnt1 > max_var):
                    max_var = cnt1
                
                if max_var is None or (cnt2 is not None and cnt2 > max_var):
                    max_var = cnt2
                    
                if cnt1 < 0:
                    cnt1 = 0
                    flag1 = flag2 = False
            
            if max_var is None:
                return 0
            return max_var
        
        ans = 0
        chars = set([c for c in s])
        
        n = len(s)
        for c1 in chars:
            for c2 in chars:
                ans = max(ans, maxVar(c1,c2))
                
        return ans
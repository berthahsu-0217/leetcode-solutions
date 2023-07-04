class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        
        @cache
        def dfs(last, xcnt, ycnt, zcnt):
            
            l = 0
            if xcnt and last in (-1,1,2):
                l = max(l, dfs(0, xcnt-1, ycnt, zcnt)+2)
            if ycnt and last in (-1,0):
                l = max(l, dfs(1, xcnt, ycnt-1, zcnt)+2)
            if zcnt and last in (-1,1,2):
                l = max(l, dfs(2, xcnt, ycnt, zcnt-1)+2)
            
            return l
        
        return dfs(-1, x, y, z)
        
        
        
        
        
        
        
        
        
        
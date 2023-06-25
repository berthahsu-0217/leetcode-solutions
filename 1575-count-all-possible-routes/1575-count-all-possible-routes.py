class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        MOD = 1000000007
        n = len(locations)
        
        @cache
        def dfs(i, fuel):
            r = int(i == finish)
            if fuel == 0:
                return r
            for j in range(n):
                if j != i and abs(locations[i]-locations[j]) <= fuel:
                    r += dfs(j, fuel-abs(locations[i]-locations[j]))
                    r %= MOD
            return r
        
        return dfs(start, fuel)
            
        
        
        
        